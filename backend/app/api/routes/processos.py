from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import List, Optional
from app.core.database import get_db
from app.models.processo import Processo
from app.models.operador import Operador
from app.models.maquinario import Maquinario
from app.models.aviamento import Aviamento
from app.schemas.processo import (
    ProcessoCreate, 
    ProcessoResponse, 
    ProcessoUpdate,
    ProcessoStatusUpdate
)

router = APIRouter(prefix="/processos", tags=["Processos"])

@router.post("/", response_model=ProcessoResponse, status_code=status.HTTP_201_CREATED)
async def criar_processo(
    processo: ProcessoCreate,
    db: AsyncSession = Depends(get_db)
):
    """Cria um novo processo (RF004)"""
    
    # Validar se os operadores existem
    if processo.operadores_ids:
        for op_id in processo.operadores_ids:
            query = select(Operador).where(
                Operador.id == op_id,
                Operador.ativo == True
            )
            result = await db.execute(query)
            if not result.scalar_one_or_none():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Operador {op_id} não encontrado ou inativo"
                )
    
    # Validar se os maquinários existem e estão disponíveis
    if processo.maquinarios_ids:
        for maq_id in processo.maquinarios_ids:
            query = select(Maquinario).where(
                Maquinario.id == maq_id,
                Maquinario.ativo == True,
                Maquinario.status == "Ativo"
            )
            result = await db.execute(query)
            maq = result.scalar_one_or_none()
            if not maq:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Maquinário {maq_id} não disponível (inexistente, inativo ou em manutenção)"
                )
    
    # Validar se os aviamentos existem
    if processo.aviamentos_ids:
        for av_id in processo.aviamentos_ids:
            query = select(Aviamento).where(
                Aviamento.id == av_id,
                Aviamento.ativo == True
            )
            result = await db.execute(query)
            if not result.scalar_one_or_none():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Aviamento {av_id} não encontrado ou inativo"
                )
    
    # Criar novo processo
    db_processo = Processo(**processo.model_dump())
    db.add(db_processo)
    await db.commit()
    await db.refresh(db_processo)
    return db_processo

@router.get("/", response_model=List[ProcessoResponse])
async def listar_processos(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    tipo: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Lista todos os processos com filtros opcionais"""
    query = select(Processo).offset(skip).limit(limit)
    
    if status:
        query = query.where(Processo.status == status)
    
    if tipo:
        query = query.where(Processo.tipo == tipo)
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{processo_id}", response_model=ProcessoResponse)
async def obter_processo(
    processo_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Obtém um processo pelo ID"""
    query = select(Processo).where(Processo.id == processo_id)
    result = await db.execute(query)
    processo = result.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    return processo

@router.put("/{processo_id}", response_model=ProcessoResponse)
async def atualizar_processo(
    processo_id: str,
    processo_update: ProcessoUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Atualiza um processo existente"""
    query = select(Processo).where(Processo.id == processo_id)
    result = await db.execute(query)
    processo = result.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    
    # Se for atualizar status, verificar regras
    if processo_update.status:
        if processo.status == "Encerrado" and processo_update.status != "Encerrado":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Processo encerrado não pode ser reativado"
            )
    
    # Atualizar apenas campos fornecidos
    for key, value in processo_update.model_dump(exclude_unset=True).items():
        setattr(processo, key, value)
    
    await db.commit()
    await db.refresh(processo)
    return processo

@router.patch("/{processo_id}/status", response_model=ProcessoResponse)
async def atualizar_status_processo(
    processo_id: str,
    status_update: ProcessoStatusUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Atualiza apenas o status do processo (executar, pausar, encerrar)"""
    query = select(Processo).where(Processo.id == processo_id)
    result = await db.execute(query)
    processo = result.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    
    # Validar transição de status
    if processo.status == "Encerrado":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Processo encerrado não pode ter status alterado"
        )
    
    processo.status = status_update.status
    await db.commit()
    await db.refresh(processo)
    return processo

@router.delete("/{processo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_processo(
    processo_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Remove um processo (apenas se estiver encerrado)"""
    query = select(Processo).where(Processo.id == processo_id)
    result = await db.execute(query)
    processo = result.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    
    # Regra de negócio: só pode remover processos encerrados
    if processo.status not in ["Encerrado", "Nenhum"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Apenas processos encerrados ou não iniciados podem ser removidos"
        )
    
    processo.ativo = False
    await db.commit()