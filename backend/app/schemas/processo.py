from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Optional
import re

class ProcessoBase(BaseModel):
    nome: str = Field(..., max_length=60)
    tipo: str = Field(..., max_length=30)
    tempo_execucao: str = Field(..., pattern="^([0-9]{2}):([0-9]{2}):([0-9]{2})$")
    operadores_ids: List[str] = Field(default_factory=list)
    maquinarios_ids: List[str] = Field(default_factory=list)
    aviamentos_ids: List[str] = Field(default_factory=list)

    @validator('tempo_execucao')
    def validar_tempo(cls, v):
        if not re.match(r'^\d{2}:\d{2}:\d{2}$', v):
            raise ValueError('Formato deve ser HH:MM:SS')
        return v

class ProcessoCreate(ProcessoBase):
    pass

class ProcessoUpdate(BaseModel):
    nome: Optional[str] = Field(None, max_length=60)
    tipo: Optional[str] = Field(None, max_length=30)
    status: Optional[str] = Field(None, max_length=20)
    tempo_execucao: Optional[str] = Field(None, pattern="^([0-9]{2}):([0-9]{2}):([0-9]{2})$")
    operadores_ids: Optional[List[str]] = None
    maquinarios_ids: Optional[List[str]] = None
    aviamentos_ids: Optional[List[str]] = None
    ativo: Optional[bool] = None

class ProcessoResponse(ProcessoBase):
    id: str
    status: str
    ativo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProcessoStatusUpdate(BaseModel):
    status: str = Field(..., pattern="^(Em execução|Pausado|Encerrado)$")