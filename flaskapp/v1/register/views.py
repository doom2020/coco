from flaskapp.v1.register.actions import RegisterHandler
from flaskapp.http_response import CreateResponse
from flaskapp.param_check import ParamCheck, SpecialCheck
from flask import Blueprint



register_bp = Blueprint('register_api', __name__, url_prefix='/api/v1')

@register_bp.route('/register', methods=['POST'])
def register_view():
    # 参数校验
    param_check = ParamCheck()
    param_check.params_add('register_type', required=True, p_type='int', err_msg='register_type is error')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    register_type = param_check.get_argv('register_type')
    # 特殊参数校验
    flag, cm, msg = SpecialCheck(register_type, err_msg='register type error').check_register_type()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    register_handler = RegisterHandler(register_type)

