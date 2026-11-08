from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class UsuarioBase(BaseModel):
    email: EmailStr
    nome: str = Field(..., max_length=100)


class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=8, max_length=100)
    is_admin: bool = False


class UsuarioResponse(UsuarioBase):
    id: str
    is_admin: bool
    ativo: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str