import pytest
from httpx import AsyncClient
from tests.conftest import admin_token

@pytest.mark.asyncio
async def test_nao_remover_processo_em_execucao(client: AsyncClient, admin_token: str):
    """Não deve permitir remover processo com status 'Em execução'."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Cria um processo
    payload = {
        "nome": "Processo Teste",
        "tipo": "Produção",
        "tempo_execucao": "01:00:00"
    }
    response = await client.post("/api/v1/processos/", json=payload, headers=headers)
    proc_id = response.json()["id"]
    
    # Muda o status para "Em execução"
    await client.patch(f"/api/v1/processos/{proc_id}/status", json={"status": "Em execução"}, headers=headers)
    
    # Tenta remover
    response_delete = await client.delete(f"/api/v1/processos/{proc_id}", headers=headers)
    assert response_delete.status_code == 400
    assert "Apenas processos encerrados ou não iniciados podem ser removidos" in response_delete.json()["detail"]

@pytest.mark.asyncio
async def test_ciclo_de_vida_processo(client: AsyncClient, admin_token: str):
    """Testa a transição de status: Nenhum -> Em execução -> Pausado -> Encerrado."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Cria processo
    payload = {"nome": "Ciclo", "tipo": "Produção", "tempo_execucao": "02:00:00"}
    response = await client.post("/api/v1/processos/", json=payload, headers=headers)
    proc_id = response.json()["id"]
    
    # Executar
    res_exec = await client.patch(f"/api/v1/processos/{proc_id}/status", json={"status": "Em execução"}, headers=headers)
    assert res_exec.json()["status"] == "Em execução"
    
    # Pausar
    res_pause = await client.patch(f"/api/v1/processos/{proc_id}/status", json={"status": "Pausado"}, headers=headers)
    assert res_pause.json()["status"] == "Pausado"
    
    # Encerrar
    res_finish = await client.patch(f"/api/v1/processos/{proc_id}/status", json={"status": "Encerrado"}, headers=headers)
    assert res_finish.json()["status"] == "Encerrado"