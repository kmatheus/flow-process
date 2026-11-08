import pytest
from httpx import AsyncClient
from tests.factories import OperadorFactory

@pytest.mark.asyncio
async def test_criar_operador_sem_autenticacao(client: AsyncClient):
    """Deve retornar 401 se não enviar token."""
    response = await client.post("/api/v1/operadores/", json={})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_criar_operador_com_autenticacao(client: AsyncClient, db_session):
    """Deve criar o operador se estiver autenticado."""
    from app.models.usuario import Usuario
    from app.core.security import gerar_hash_senha
    from app.core.security import criar_access_token
    
    # 1. Cria um usuário admin no banco de teste
    admin = Usuario(
        email="admin@teste.com",
        senha_hash=gerar_hash_senha("senha123"),
        nome="Admin Teste",
        is_admin=True
    )
    db_session.add(admin)
    await db_session.commit()
    
    # 2. Gera o token para esse admin
    token = criar_access_token(subject=str(admin.id))
    
    # 3. Cria os dados falsos do operador
    operador_data = OperadorFactory()
    
    payload = {
        "nome_completo": operador_data.nome_completo,
        "data_nascimento": operador_data.data_nascimento.isoformat(),
        "cpf": operador_data.cpf,
        "telefone1": operador_data.telefone1
    }
    
    # 4. Faz a requisição COM o token
    response = await client.post(
        "/api/v1/operadores/",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # 5. Verifica se deu certo
    assert response.status_code == 201
    data = response.json()
    assert data["nome_completo"] == payload["nome_completo"]
    assert data["cpf"] == payload["cpf"]