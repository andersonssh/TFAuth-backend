"""
authentication module
"""
import jwt
import datetime


def token_generate(user: dict):
    """
    #####################
    """
    exp = (datetime.datetime.now() + datetime.timedelta(seconds=20)).timestamp()
    payload = {
        key: value for key, value in user.items() if key in ('username',)
    }

    return jwt.encode(jwt)
