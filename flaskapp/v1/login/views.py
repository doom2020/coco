from flask import Blueprint
from flaskapp.param_check import ParamCheck, SpecialCheck
from flaskapp.http_response import CreateResponse
from flaskapp.enumeration import *
from flaskapp.v1.login.actions import LoginFactory


login_bp = Blueprint('login_api', __name__, url_prefix='/api/v1')


@login_bp.route('/to_login', methods=['GET'])
def to_login_view():
    return 'login get'


@login_bp.route('/login', methods=['POST'])
def login_view():
    """
    3种登录情况,房东,租户,平台人员
    :return:
    """
    param_check = ParamCheck()
    param_check.params_add('login_type', required=True, p_type='str', err_msg='')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    login_type = param_check.get_argv('login_type')
    # 登录类型特殊参数校验
    flag, cm, msg = SpecialCheck(login_type, err_msg='login type is invalid ').check_login_type()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    param_check.params_add('login_method', required=True, p_type='str', err_msg='')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    login_method = param_check.get_argv('login_method')
    # 登录方式特殊校验
    flag, cm, msg = SpecialCheck(login_method, err_msg='login method is invalid').check_login_method()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    if login_type == RegisterEnum.user.value:
        # 平台人员登录
        param_check.params_add('nick_name', required=True, p_type='str', err_msg='')
        param_check.params_add('password', required=True, p_type='str', err_msg='')
        param_check.params_add('check_code', required=True, p_type='str', err_msg='')
        user_name = param_check.get_argv('user_name')
        password = param_check.get_argv('password')
        check_code = param_check.get_argv('check_code')
        param_dict = dict(user_name=user_name, password=password, check_code=check_code)
        flag, cm, msg = LoginFactory().deal_with_login(login_type).login_by_account(**param_dict)
        return CreateResponse(cm, message=msg).response()
    else:
        # 房东或者租客登录
        if login_method == LoginMethodEnum.account.value:
            # 账号登录
            param_check.params_add('nick_name', required=True, p_type='str', err_msg='')
            param_check.params_add('password', required=True, p_type='str', err_msg='')
            param_check.params_add('check_code', required=True, p_type='str', err_msg='')
            nick_name = param_check.get_argv('nick_name')
            password = param_check.get_argv('password')
            check_code = param_check.get_argv('check_code')
            param_dict = dict(nick_name=nick_name, password=password, check_code=check_code)
            flag, cm, msg = LoginFactory().deal_with_login(login_type).login_by_account(**param_dict)
            return CreateResponse(cm, message=msg).response()
        else:
            # 手机登录
            param_check.params_add('phone', required=True, p_type='str', err_msg='')
            param_check.params_add('auth_code', required=True, p_type='str', err_msg='')
            param_check.params_add('check_code', required=True, p_type='str', err_msg='')
            phone = param_check.get_argv('phone')
            auth_code = param_check.get_argv('auth_code')
            check_code = param_check.get_argv('check_code')
            param_dict = dict(phone=phone, auth_code=auth_code, check_code=check_code)
            flag, cm, msg = LoginFactory().deal_with_login(login_type).login_by_phone(**param_dict)
            return CreateResponse(cm, message=msg).response()


