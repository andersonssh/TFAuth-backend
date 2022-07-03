from flask import Blueprint, request
from src.http_utils import status_code, validate_content
code_bp = Blueprint('code_bp', __name__, url_prefix='/code')

@code_bp.route('/', methods=['GET'])
def code():

    return {'code': ''}
