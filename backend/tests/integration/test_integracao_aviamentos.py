import pytest
from httpx import AsyncClient
from tests.conftest import admin_token

@pytest.mark.asyncio
async def test_movimentacao_estoque_saldo_insuficiente(client: AsyncClient, admin_token: str):
    """Não deve permitir saída maior que o estoque atual."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Cria aviamento com 10 unidades
    payload = {
        "codigo_produto": "AVI001",
        "nome": "Linha",
        "categoria": "Costura",
        "fornecedor": "Fornecedor X",
        "valor": 5.0,
        "data_aquisicao": "2026-01-01",
        "quantidade": 10
    }
    response = await client.post("/api/v1/aviamentos/", json=payload, headers=headers)
    av_id = response.json()["id"]
    
    # Tenta saída de 20 unidades
    mov_payload = {"tipo": "saida", "quantidade": 20}
    response_saida = await client.post(f"/api/v1/aviamentos/{av_id}/movimentar", json=mov_payload, headers=headers)
    
    assert response_saida.status_code == 400
    assert response_saida.json()["detail"] == "Quantidade insuficiente em estoque"

@pytest.mark.asyncio
async def test_movimentacao_estoque_sucesso(client: AsyncClient, admin_token: str):
    """Deve atualizar o estoque corretamente após movimentação."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Cria aviamento
    payload = {
        "codigo_produto": "AVI002", "nome": "Botão", "categoria": "Acessórios",
        "fornecedor": "F", "valor": 1.0, "data_aquisicao": "2026-01-01", "quantidade": 50
    }
    response = await client.post("/api/v1/aviamentos/", json=payload, headers=headers)
    av_id = response.json()["id"]
    
    # Saída de 10
    await client.post(f"/api/v1/aviamentos/{av_id}/movimentar", json={"tipo": "saida", "quantidade": 10}, headers=headers)
    
    # Verifica o estoque
    response_get = await client.get(f"/api/v1/aviamentos/{av_id}", headers=headers)
    assert response_get.json()["quantidade"] == 40