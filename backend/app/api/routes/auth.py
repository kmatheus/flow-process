from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.core.security import (
    verificar_senha,
    gerar_hash_senha,
    criar_access_token,
    criar_refresh_token,
)
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.schemas.token import Token
from app.api.dependencies import get_current_admin

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/register", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def registrar_usuario(
    usuario: UsuarioCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: Usuario = Depends(get_current_admin)  # Apenas admins podem cadastrar
):
    """Registra um novo usuário (apenas administradores)."""
    # Verificar se email já existe
    query = select(Usuario).where(Usuario.email == usuario.email)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
    
    # Criar novo usuário
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
    # Buscar usuário pelo email
    query = select(Usuario).where(Usuario.email == form_data.username)
    result = await db.execute(query)
    usuario = result.scalar_one_or_none()
    
    # Verificar credenciais
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
    
    # Gerar tokens
    access_token = criar_access_token(subject=usuario.id)
    refresh_token = criar_refresh_token(subject=usuario.id)
    
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )