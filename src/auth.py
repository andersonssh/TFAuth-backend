"""
authentication module
"""
import datetime
import utoken
from api import SECRET_KEY


def token_generate(user: dict):
    """
    Gera o token com informacoes do usuario

    Args:
        user: dados do usuario

    Returns:
        str: token
    """

    exp = datetime.datetime.now() + datetime.timedelta(days=1)
    payload = {}

    if user.get('email'):
        payload['email'] = user.get('email')

    token_content = {'max-time': exp}
    token_content.update(payload)

    return utoken.encode(token_content, SECRET_KEY)
