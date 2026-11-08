from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.core.security import decodificar_token
from app.core.redis_config import get_redis
from app.models.usuario import Usuario
import redis.asyncio as aioredis

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
    redis: aioredis.Redis = Depends(get_redis)
) -> Usuario:
    """Obtém o usuário atual e verifica se o token está na blacklist."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decodificar_token(token)
    if payload is None:
        raise credentials_exception
    
    # Verificar se o token está na blacklist (se foi deslogado)
    jti = payload.get("jti")
    if jti:
        is_blacklisted = await redis.get(f"blacklist:{jti}")
        if is_blacklisted:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido (sessão encerrada)",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    if payload.get("type") != "access":
        raise credentials_exception
    
    user_id: str = payload.get("sub")
    if user_id is None:
        raise credentials_exception
    
    query = select(Usuario).where(Usuario.id == user_id, Usuario.ativo == True)
    result = await db.execute(query)
    usuario = result.scalar_one_or_none()
    
    if usuario is None:
        raise credentials_exception
    
    return usuario


async def get_current_admin(
    current_user: Usuario = Depends(get_current_user)
) -> Usuario:
    """Verifica se o usuário atual é administrador."""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso restrito a administradores"
        )
    return current_user