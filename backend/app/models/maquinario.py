import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Date
from sqlalchemy.sql import func
from app.core.database import Base

class Maquinario(Base):
    __tablename__ = "maquinarios"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    numero = Column(String(20), unique=True, nullable=False)
    nome = Column(String(80), nullable=False)
    modelo = Column(String(60), nullable=False)
    valor = Column(String(20), nullable=True)
    data_aquisicao = Column(Date, nullable=True)
    tipo = Column(String(20), nullable=True)  # "Próprio" ou "Terceiro"
    status = Column(String(20), default="Ativo")  # Ativo, Manutenção, Baixado
    descricao = Column(String(150), nullable=True)
    ativo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Maquinario {self.nome} - {self.numero}>"