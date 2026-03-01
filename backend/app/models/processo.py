import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Float, JSON, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Processo(Base):
    __tablename__ = "processos"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String(60), nullable=False)
    tipo = Column(String(30), nullable=False)
    status = Column(String(20), default="Nenhum")  # Nenhum, Em execução, Pausado, Encerrado
    tempo_execucao = Column(String(8), nullable=False)  # Formato HH:MM:SS
    
    # Relacionamentos (armazenados como JSON para simplificar)
    operadores_ids = Column(JSON, default=list)  # Lista de IDs dos operadores
    maquinarios_ids = Column(JSON, default=list)  # Lista de IDs dos maquinários
    aviamentos_ids = Column(JSON, default=list)  # Lista de IDs dos aviamentos
    
    ativo = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Processo {self.nome} - {self.status}>"