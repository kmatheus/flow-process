from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone
from app.core.database import get_db
from app.core.security import (
    verificar_senha,
    gerar_hash_senha,
    criar_access_token,
    criar_refresh_token,
    decodificar_token
)
from app.core.redis_config import get_redis
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.schemas.token import Token
from app.api.dependencies import get_current_admin, get_current_user, oauth2_scheme
import redis.asyncio as aioredis

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def registrar_usuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: Usuario = Depends(get_current_admin)
):
    """Registra um novo usuário (apenas administradores)."""
    query = select(Usuario).where(Usuario.email == usuario.email)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    db_usuario = Usuario(
        email=usuario.email,
        senha_hash=gerar_hash_senha(usuario.senha),
        nome=usuario.nome,
        is_admin=usuario.is_admin,
        ativo=True
    )
    db.add(db_usuario)
    await db.commit()
    await db.refresh(db_usuario)
    return db_usuario


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    """Autentica um usuário e retorna os tokens de acesso."""
    query = select(Usuario).where(Usuario.email == form_data.username)
    result = await db.execute(query)
    usuario = result.scalar_one_or_none()
    
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not usuario.ativo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo"
        )
    
    access_token = criar_access_token(subject=usuario.id)
    refresh_token = criar_refresh_token(subject=usuario.id)
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )


@router.post("/refresh", response_model=Token)
async def refresh_token(
    refresh_token_str: str,
    db: AsyncSession = Depends(get_db),
    redis: aioredis.Redis = Depends(get_redis)
):
    """Renova o access_token usando um refresh_token válido."""
    payload = decodificar_token(refresh_token_str)
    
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token inválido"
        )
    
    jti = payload.get("jti")
    if jti:
        is_blacklisted = await redis.get(f"blacklist:{jti}")
        if is_blacklisted:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token já foi utilizado ou revogado"
            )
    
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token inválido"
        )
    
    query = select(Usuario).where(Usuario.id == user_id, Usuario.ativo == True)
    result = await db.execute(query)
    usuario = result.scalar_one_or_none()
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado ou inativo"
        )
    
    if jti:
        exp = payload.get("exp")
        if exp:
            exp_datetime = datetime.fromtimestamp(exp, tz=timezone.utc)
            now = datetime.now(timezone.utc)
            ttl = int((exp_datetime - now).total_seconds())
            if ttl > 0:
                await redis.setex(f"blacklist:{jti}", ttl, "revoked")
    
    new_access_token = criar_access_token(subject=usuario.id)
    new_refresh_token = criar_refresh_token(subject=usuario.id)
    
    return Token(
        access_token=new_access_token,
        refresh_token=new_refresh_token,
        token_type="bearer"
    )


@router.post("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    redis: aioredis.Redis = Depends(get_redis)
):
    """Faz logout adicionando o token atual à blacklist do Redis."""
    payload = decodificar_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token inválido"
        )
    
    jti = payload.get("jti")
    exp = payload.get("exp")
    
    if jti and exp:
        exp_datetime = datetime.fromtimestamp(exp, tz=timezone.utc)
        now = datetime.now(timezone.utc)
        ttl = int((exp_datetime - now).total_seconds())
        
        if ttl > 0:
            await redis.setex(f"blacklist:{jti}", ttl, "revoked")
            
    return {"message": "Logout realizado com sucesso"}