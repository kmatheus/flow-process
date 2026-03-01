from pydantic import BaseModel, Field, validator
from datetime import date, datetime
from typing import Optional

class AviamentoBase(BaseModel):
    codigo_produto: str = Field(..., max_length=20)
    nome: str = Field(..., max_length=80)
    categoria: str = Field(..., max_length=60)
    fornecedor: str = Field(..., max_length=80)
    valor: float = Field(..., gt=0)
    data_aquisicao: date
    quantidade: int = Field(..., ge=0)
    marca: Optional[str] = Field(None, max_length=60)
    descricao: Optional[str] = Field(None, max_length=150)

    @validator('valor')
    def validar_valor(cls, v):
        if v <= 0:
            raise ValueError('Valor deve ser maior que zero')
        return v

class AviamentoCreate(AviamentoBase):
    pass

class AviamentoUpdate(BaseModel):
    codigo_produto: Optional[str] = Field(None, max_length=20)
    nome: Optional[str] = Field(None, max_length=80)
    categoria: Optional[str] = Field(None, max_length=60)
    fornecedor: Optional[str] = Field(None, max_length=80)
    valor: Optional[float] = Field(None, gt=0)
    data_aquisicao: Optional[date] = None
    quantidade: Optional[int] = Field(None, ge=0)
    marca: Optional[str] = Field(None, max_length=60)
    descricao: Optional[str] = Field(None, max_length=150)
    ativo: Optional[bool] = None

class AviamentoResponse(AviamentoBase):
    id: str
    ativo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class AviamentoMovimentacao(BaseModel):
    tipo: str = Field(..., pattern="^(entrada|saida)$")
    quantidade: int = Field(..., gt=0)
    observacao: Optional[str] = Field(None, max_length=200)