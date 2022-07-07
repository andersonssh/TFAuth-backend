"""
authentication module
"""
import datetime
import jwt
from api import SECRET_KEY


def token_generate(user: dict):
    """
    Gera o token JWT com informacoes do usuario

    Args:
        user: dados do usuario

    Returns:
        str: token
    """

    exp = datetime.datetime.now() + datetime.timedelta(days=1)
    payload = {}

    if user.get('email'):
        payload['email'] = user.get('email')

    token_content = {'exp': exp}
    token_content.update(payload)

    return jwt.encode(token_content, key=SECRET_KEY, algorithm='HS256')
