from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional
from app.core.database import get_db
from app.models.maquinario import Maquinario
from app.schemas.maquinario import MaquinarioCreate, MaquinarioResponse, MaquinarioUpdate

router = APIRouter(prefix="/maquinarios", tags=["Maquinários"])

@router.post("/", response_model=MaquinarioResponse, status_code=status.HTTP_201_CREATED)
async def criar_maquinario(
    maquinario: MaquinarioCreate,
    db: AsyncSession = Depends(get_db)
):
    """Cria um novo maquinário (RF002)"""
    # Verificar se número já existe
    query = select(Maquinario).where(Maquinario.numero == maquinario.numero)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Número de maquinário já cadastrado"
        )
    
    # Criar novo maquinário
    db_maquinario = Maquinario(**maquinario.model_dump())
    db.add(db_maquinario)
    await db.commit()
    await db.refresh(db_maquinario)
    return db_maquinario

@router.get("/", response_model=List[MaquinarioResponse])
async def listar_maquinarios(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Lista todos os maquinários com filtro opcional por status"""
    query = select(Maquinario).offset(skip).limit(limit)
    
    if status:
        query = query.where(Maquinario.status == status)
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{maquinario_id}", response_model=MaquinarioResponse)
async def obter_maquinario(
    maquinario_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Obtém um maquinário pelo ID"""
    query = select(Maquinario).where(Maquinario.id == maquinario_id)
    result = await db.execute(query)
    maquinario = result.scalar_one_or_none()
    
    if not maquinario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maquinário não encontrado"
        )
    return maquinario

@router.put("/{maquinario_id}", response_model=MaquinarioResponse)
async def atualizar_maquinario(
    maquinario_id: str,
    maquinario_update: MaquinarioUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Atualiza um maquinário existente"""
    query = select(Maquinario).where(Maquinario.id == maquinario_id)
    result = await db.execute(query)
    maquinario = result.scalar_one_or_none()
    
    if not maquinario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maquinário não encontrado"
        )
    
    # Se estiver tentando mudar o número, verificar se já existe
    if maquinario_update.numero and maquinario_update.numero != maquinario.numero:
        query_numero = select(Maquinario).where(Maquinario.numero == maquinario_update.numero)
        result_numero = await db.execute(query_numero)
        if result_numero.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Número de maquinário já cadastrado"
            )
    
    # Atualizar apenas campos fornecidos
    for key, value in maquinario_update.model_dump(exclude_unset=True).items():
        setattr(maquinario, key, value)
    
    await db.commit()
    await db.refresh(maquinario)
    return maquinario

@router.delete("/{maquinario_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_maquinario(
    maquinario_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Remove um maquinário (soft delete)"""
    query = select(Maquinario).where(Maquinario.id == maquinario_id)
    result = await db.execute(query)
    maquinario = result.scalar_one_or_none()
    
    if not maquinario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maquinário não encontrado"
        )
    
    # Soft delete (apenas marca como inativo)
    maquinario.ativo = False
    await db.commit()