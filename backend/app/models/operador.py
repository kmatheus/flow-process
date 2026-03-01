from sqlalchemy import Column, String, Boolean, DateTime, Date
from sqlalchemy.sql import func
from app.core.database import Base
import uuid

class Operador(Base):
    __tablename__ = "operadores"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome_completo = Column(String(60), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    telefone1 = Column(String(11), nullable=False)
    telefone2 = Column(String(11), nullable=True)
    email = Column(String(100), nullable=True)
    funcoes = Column(String(500), nullable=True)  # JSON string
    ativo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Operador {self.nome_completo}>"