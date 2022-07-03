"""
utils related to http protocol
"""
from types import FunctionType
from functools import wraps
from flask import request
from http import HTTPStatus as status_code
import jsonschema

MAX_CONTENT_LENGTH = 10**5


def validate_content(schema: dict):
    """
    Decorator para validar o conteudo de uma requisicao baseado no schema

    Args:
        schema: schema in jsonschema
    """
    def decorator(func: FunctionType):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.content_type != 'application/json':
                return {'message': status_code.UNSUPPORTED_MEDIA_TYPE.phrase},\
                       status_code.UNSUPPORTED_MEDIA_TYPE
            if request.content_length > MAX_CONTENT_LENGTH:
                return {'message': status_code.REQUEST_ENTITY_TOO_LARGE.phrase},\
                        status_code.REQUEST_ENTITY_TOO_LARGE

            try:
                jsonschema.validate(instance=request.json, schema=schema)
            except jsonschema.ValidationError as error:
                return {'message': error.message},\
                        status_code.BAD_REQUEST

            return func(*args, *kwargs)

        return wrapper
    return decorator