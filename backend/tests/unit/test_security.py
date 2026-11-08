from app.core.security import gerar_hash_senha, verificar_senha, criar_access_token, decodificar_token

def test_gerar_e_verificar_senha():
    senha = "minha_senha_secreta"
    hash_gerado = gerar_hash_senha(senha)
    
    # O hash não deve ser igual à senha
    assert hash_gerado != senha
    # A verificação deve funcionar
    assert verificar_senha(senha, hash_gerado) is True
    # Senha errada deve falhar
    assert verificar_senha("senha_errada", hash_gerado) is False

def test_criar_e_decodificar_token():
    user_id = "1234-5678"
    token = criar_access_token(subject=user_id)
    
    payload = decodificar_token(token)
    
    assert payload is not None
    assert payload["sub"] == user_id
    assert payload["type"] == "access"
    assert "jti" in payload