from flask import Blueprint

index_bp = Blueprint('index_api', __name__, url_prefix='/v1/api')

@index_bp.route('/', methods=['GET'])
def index_view():
    return "hello world"