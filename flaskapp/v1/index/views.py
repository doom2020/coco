from flask import Blueprint
from flask.json import jsonify
from flaskapp.param_check import ParamCheck


index_bp = Blueprint('index_api', __name__, url_prefix='/v1/api')


@index_bp.route('/', methods=['POST'])
def index_view():
    # 参数校验
    param_check = ParamCheck()
    param_check.params_add('name', required=True, p_type='str', msg='')
    param_check.params_add('age', required=True, p_type='int', msg='')
    param_check.params_add('height', required=True, p_type='float', msg='')
    param_check.params_add('like', required=True, p_type='list', msg='')
    param_check.params_add('info', required=True, p_type='dict', msg='')
    flag, ret_dict = param_check.params_parser()
    if not flag:
        return jsonify(ret_dict)
    name = param_check.get_argv('name')
    age = param_check.get_argv('age')
    height = param_check.get_argv('height')
    like = param_check.get_argv('like')
    info = param_check.get_argv('info')
    # 逻辑处理

    # 正常响应
    return jsonify(code=200, success=True, result={}, message='')