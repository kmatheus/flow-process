import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_logout_e_blacklist(client: AsyncClient, db_session):
    """Deve invalidar o token após logout."""
    from app.models.usuario import Usuario
    from app.core.security import gerar_hash_senha, criar_access_token
    
    # Cria usuário
    user = Usuario(email="logout@teste.com", senha_hash=gerar_hash_senha("123"), nome="Logout", is_admin=True)
    db_session.add(user)
    await db_session.commit()
    
    # Gera token
    token = criar_access_token(subject=str(user.id))
    headers = {"Authorization": f"Bearer {token}"}
    
    # Testa acesso (deve dar 200)
    response_before = await client.get("/api/v1/operadores/", headers=headers)
    assert response_before.status_code == 200
    
    # Faz logout
    response_logout = await client.post("/api/v1/auth/logout", headers=headers)
    assert response_logout.status_code == 200
    
    # Tenta acessar novamente (deve dar 401)
    response_after = await client.get("/api/v1/operadores/", headers=headers)
    assert response_after.status_code == 401
    assert "sessão encerrada" in response_after.json()["detail"].lower()