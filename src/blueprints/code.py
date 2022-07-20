from flask import Blueprint, request
code_bp = Blueprint('code_bp', __name__, url_prefix='/code')


@code_bp.route('/')
def code():
    return {'code': ''}
