"""
Testa funcoes de autenticacao
"""
import jwt
from src import auth
from api import SECRET_KEY


def test_jwt_token_creation_with_correct_fields(mock_user):
    """
    Verifica se o token jwt é criado com os campos corretos
    """
    expected_token_fields = {'email', 'exp'}
    token = auth.token_generate(mock_user)
    decoded_token = jwt.decode(token, key=SECRET_KEY, algorithms=['HS256'])
    token_fields = set(decoded_token.keys())

    assert token_fields == expected_token_fields

