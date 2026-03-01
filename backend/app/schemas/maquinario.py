from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional

class MaquinarioBase(BaseModel):
    numero: str = Field(..., max_length=20)
    nome: str = Field(..., max_length=80)
    modelo: str = Field(..., max_length=60)
    valor: Optional[str] = Field(None, max_length=20)
    data_aquisicao: Optional[date] = None
    tipo: Optional[str] = Field(None, max_length=20)
    status: str = Field("Ativo", max_length=20)
    descricao: Optional[str] = Field(None, max_length=150)

class MaquinarioCreate(MaquinarioBase):
    pass

class MaquinarioUpdate(BaseModel):
    numero: Optional[str] = Field(None, max_length=20)
    nome: Optional[str] = Field(None, max_length=80)
    modelo: Optional[str] = Field(None, max_length=60)
    valor: Optional[str] = Field(None, max_length=20)
    data_aquisicao: Optional[date] = None
    tipo: Optional[str] = Field(None, max_length=20)
    status: Optional[str] = Field(None, max_length=20)
    descricao: Optional[str] = Field(None, max_length=150)
    ativo: Optional[bool] = None

class MaquinarioResponse(MaquinarioBase):
    id: str
    ativo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True