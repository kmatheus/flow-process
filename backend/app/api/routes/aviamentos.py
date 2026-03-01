from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import List, Optional
from app.core.database import get_db
from app.models.aviamento import Aviamento
from app.schemas.aviamento import (
    AviamentoCreate, 
    AviamentoResponse, 
    AviamentoUpdate,
    AviamentoMovimentacao
)

router = APIRouter(prefix="/aviamentos", tags=["Aviamentos/Recursos"])

@router.post("/", response_model=AviamentoResponse, status_code=status.HTTP_201_CREATED)
async def criar_aviamento(
    aviamento: AviamentoCreate,
    db: AsyncSession = Depends(get_db)
):
    """Cria um novo aviamento/recurso (RF003)"""
    # Verificar se código do produto já existe
    query = select(Aviamento).where(Aviamento.codigo_produto == aviamento.codigo_produto)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Código do produto já cadastrado"
        )
    
    # Criar novo aviamento
    db_aviamento = Aviamento(**aviamento.model_dump())
    db.add(db_aviamento)
    await db.commit()
    await db.refresh(db_aviamento)
    return db_aviamento

@router.get("/", response_model=List[AviamentoResponse])
async def listar_aviamentos(
    skip: int = 0,
    limit: int = 100,
    categoria: Optional[str] = None,
    nome: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """Lista todos os aviamentos com filtros opcionais"""
    query = select(Aviamento).offset(skip).limit(limit)
    
    if categoria:
        query = query.where(Aviamento.categoria == categoria)
    
    if nome:
        query = query.where(Aviamento.nome.ilike(f"%{nome}%"))
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{aviamento_id}", response_model=AviamentoResponse)
async def obter_aviamento(
    aviamento_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Obtém um aviamento pelo ID"""
    query = select(Aviamento).where(Aviamento.id == aviamento_id)
    result = await db.execute(query)
    aviamento = result.scalar_one_or_none()
    
    if not aviamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aviamento não encontrado"
        )
    return aviamento

@router.put("/{aviamento_id}", response_model=AviamentoResponse)
async def atualizar_aviamento(
    aviamento_id: str,
    aviamento_update: AviamentoUpdate,
    db: AsyncSession = Depends(get_db)
):
    """Atualiza um aviamento existente"""
    query = select(Aviamento).where(Aviamento.id == aviamento_id)
    result = await db.execute(query)
    aviamento = result.scalar_one_or_none()
    
    if not aviamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aviamento não encontrado"
        )
    
    # Se estiver tentando mudar o código, verificar se já existe
    if (aviamento_update.codigo_produto and 
        aviamento_update.codigo_produto != aviamento.codigo_produto):
        query_codigo = select(Aviamento).where(
            Aviamento.codigo_produto == aviamento_update.codigo_produto
        )
        result_codigo = await db.execute(query_codigo)
        if result_codigo.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Código do produto já cadastrado"
            )
    
    # Atualizar apenas campos fornecidos
    for key, value in aviamento_update.model_dump(exclude_unset=True).items():
        setattr(aviamento, key, value)
    
    await db.commit()
    await db.refresh(aviamento)
    return aviamento

@router.post("/{aviamento_id}/movimentar")
async def movimentar_estoque(
    aviamento_id: str,
    movimentacao: AviamentoMovimentacao,
    db: AsyncSession = Depends(get_db)
):
    """Registra entrada ou saída de estoque"""
    query = select(Aviamento).where(Aviamento.id == aviamento_id)
    result = await db.execute(query)
    aviamento = result.scalar_one_or_none()
    
    if not aviamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aviamento não encontrado"
        )
    
    # Atualizar quantidade
    if movimentacao.tipo == "entrada":
        aviamento.quantidade += movimentacao.quantidade
    else:  # saída
        if aviamento.quantidade < movimentacao.quantidade:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Quantidade insuficiente em estoque"
            )
        aviamento.quantidade -= movimentacao.quantidade
    
    await db.commit()
    await db.refresh(aviamento)
    
    return {
        "message": f"Movimentação de {movimentacao.tipo} realizada com sucesso",
        "nova_quantidade": aviamento.quantidade,
        "aviamento": aviamento
    }

@router.delete("/{aviamento_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remover_aviamento(
    aviamento_id: str,
    db: AsyncSession = Depends(get_db)
):
    """Remove um aviamento (soft delete)"""
    query = select(Aviamento).where(Aviamento.id == aviamento_id)
    result = await db.execute(query)
    aviamento = result.scalar_one_or_none()
    
    if not aviamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aviamento não encontrado"
        )
    
    aviamento.ativo = False
    await db.commit()