import pytest
from httpx import AsyncClient
from app.models.usuario import Usuario
from tests.conftest import admin_token

@pytest.mark.asyncio
async def test_criar_maquinario_numero_duplicado(client: AsyncClient, admin_token: str):
    """Não deve permitir criar maquinário com número já existente."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    payload = {
        "numero": "MAQ999",
        "nome": "Máquina Teste",
        "modelo": "Modelo X"
    }
    
    # Cria o primeiro
    response1 = await client.post("/api/v1/maquinarios/", json=payload, headers=headers)
    assert response1.status_code == 201
    
    # Tenta criar o segundo com o mesmo número
    response2 = await client.post("/api/v1/maquinarios/", json=payload, headers=headers)
    assert response2.status_code == 400
    assert response2.json()["detail"] == "Número de maquinário já cadastrado"

@pytest.mark.asyncio
async def test_filtrar_maquinarios_por_status(client: AsyncClient, admin_token: str):
    """Deve filtrar maquinários por status."""
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Cria dois maquinários com status diferentes
    await client.post("/api/v1/maquinarios/", json={"numero": "MAQ001", "nome": "Ativo", "modelo": "A", "status": "Ativo"}, headers=headers)
    await client.post("/api/v1/maquinarios/", json={"numero": "MAQ002", "nome": "Manutenção", "modelo": "B", "status": "Manutenção"}, headers=headers)
    
    response = await client.get("/api/v1/maquinarios/?status=Ativo", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["numero"] == "MAQ001"