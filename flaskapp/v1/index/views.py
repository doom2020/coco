from flask import Blueprint
from flask import request
from flaskapp.param_check import ParamCheck

index_bp = Blueprint('index_api', __name__, url_prefix='/v1/api')

@index_bp.route('/', methods=['POST'])
def index_view():
    # data = request.get_json()
    # print(data)
    # print('**************************')
    param_check = ParamCheck()
    param_check.params_add('name', required=True, p_type='str', msg='')
    param_check.params_add('age', required=True, p_type='int', msg='')
    param_check.params_add('height', required=True, p_type='float', msg='')
    param_check.params_add('like', required=True, p_type='list', msg='')
    param_check.params_add('info', required=True, p_type='dict', msg='')
    param_check.params_parser()
    name = param_check.get_argv('name')
    age = param_check.get_argv('age')
    height = param_check.get_argv('height')
    like = param_check.get_argv('like')
    info = param_check.get_argv('info')
    print(f'name: {name}, age: {age}, height: {height}, like: {like}, info: {info}')
    return "hello world"