from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.core.database import get_db
from app.models.operador import Operador
from app.schemas.operador import OperadorCreate, OperadorResponse, OperadorUpdate

router = APIRouter(prefix="/operadores", tags=["Operadores"])

@router.post("/", response_model=OperadorResponse, status_code=status.HTTP_201_CREATED)
async def criar_operador(
    operador: OperadorCreate,
    db: AsyncSession = Depends(get_db)
):
    """Cria um novo operador (RF001)"""
    # Verificar se CPF já existe
    query = select(Operador).where(Operador.cpf == operador.cpf)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF já cadastrado"
        )
    
    # Criar novo operador
    db_operador = Operador(**operador.model_dump())
    db.add(db_operador)
    await db.commit()
    await db.refresh(db_operador)
    return db_operador

@router.get("/", response_model=List[OperadorResponse])
async def listar_operadores(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Lista todos os operadores"""
    query = select(Operador).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{operador_id}", response_model=OperadorResponse)
async def obter_operador(
    operador_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Obtém um operador pelo ID"""
    query = select(Operador).where(Operador.id == operador_id)
    result = await db.execute(query)
    operador = result.scalar_one_or_none()
    
    if not operador:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operador não encontrado"
        )
    return operador

@router.put("/{operador_id}", response_model=OperadorResponse)
async def atualizar_operador(
    operador_id: str,
    operador_update: OperadorUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Atualiza um operador existente"""
    query = select(Operador).where(Operador.id == operador_id)
    result = await db.execute(query)
    operador = result.scalar_one_or_none()
    
    if not operador:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operador não encontrado"
        )
    
    # Atualizar apenas campos fornecidos
    for key, value in operador_update.model_dump(exclude_unset=True).items():
        setattr(operador, key, value)
    
    await db.commit()
    await db.refresh(operador)
    return operador

@router.delete("/{operador_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_operador(
    operador_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Remove um operador (soft delete)"""
    query = select(Operador).where(Operador.id == operador_id)
    result = await db.execute(query)
    operador = result.scalar_one_or_none()
    
    if not operador:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operador não encontrado"
        )
    
    # Soft delete (apenas marca como inativo)
    operador.ativo = False
    await db.commit()