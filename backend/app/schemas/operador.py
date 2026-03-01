from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional

class OperadorBase(BaseModel):
    nome_completo: str = Field(..., max_length=60)
    data_nascimento: date
    cpf: str = Field(..., min_length=11, max_length=11)
    telefone1: str = Field(..., min_length=10, max_length=11)
    telefone2: Optional[str] = Field(None, min_length=10, max_length=11)
    email: Optional[str] = None
    funcoes: Optional[str] = None

    @validator('cpf')
    def validar_cpf(cls, v):
        if not v.isdigit():
            raise ValueError('CPF deve conter apenas números')
        return v

class OperadorCreate(OperadorBase):
    pass

class OperadorUpdate(BaseModel):
    nome_completo: Optional[str] = Field(None, max_length=60)
    telefone1: Optional[str] = Field(None, min_length=10, max_length=11)
    telefone2: Optional[str] = Field(None, min_length=10, max_length=11)
    email: Optional[str] = None
    funcoes: Optional[str] = None
    ativo: Optional[bool] = None

class OperadorResponse(OperadorBase):
    id: str
    ativo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True