import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Date, Integer, Float
from sqlalchemy.sql import func
from app.core.database import Base

class Aviamento(Base):
    __tablename__ = "aviamentos"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    codigo_produto = Column(String(20), unique=True, nullable=False)
    nome = Column(String(80), nullable=False)
    categoria = Column(String(60), nullable=False)
    fornecedor = Column(String(80), nullable=False)
    valor = Column(Float, nullable=False)
    data_aquisicao = Column(Date, nullable=False)
    quantidade = Column(Integer, nullable=False, default=0)
    marca = Column(String(60), nullable=True)
    descricao = Column(String(150), nullable=True)
    ativo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Aviamento {self.nome} - {self.codigo_produto}>"