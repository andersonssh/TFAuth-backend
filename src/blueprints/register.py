from flask import Blueprint

register_bp = Blueprint('register_bp', __name__, url_prefix='/register')


@register_bp.route('/', methods=['POST'])
def register():
    return {}
