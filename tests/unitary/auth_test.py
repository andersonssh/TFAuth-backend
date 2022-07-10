"""
Testa funcoes de autenticacao
"""
import utoken
from src import auth
from api import SECRET_KEY


def test_jwt_token_creation_with_correct_fields(mock_user):
    """
    Verifica se o token é criado com os campos corretos
    """
    expected_token_fields = {'email'}
    token = auth.token_generate(mock_user)
    decoded_token = utoken.decode(token, SECRET_KEY)
    token_fields = set(decoded_token.keys())

    assert token_fields == expected_token_fields
