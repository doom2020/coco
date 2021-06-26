from flaskapp.v1.register.actions import RegisterFactory
from flaskapp.http_response import CreateResponse
from flaskapp.param_check import ParamCheck, SpecialCheck
from flask import Blueprint
from flaskapp.enumeration import RegisterEnum


register_bp = Blueprint('register_api', __name__, url_prefix='/api/v1')


@register_bp.route('/register', methods=['POST'])
def register_view():
    # 注册类型参数校验
    param_check = ParamCheck()
    param_check.params_add('register_type', required=True, p_type='int', err_msg='register_type is error')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    register_type = param_check.get_argv('register_type')
    # 注册类型特殊参数校验
    flag, cm, msg = SpecialCheck(register_type, err_msg='register type error').check_register_type()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    # 注册信息参数校验
    param_check.params_add('user_name', required=True, p_type='str', err_msg='')
    param_check.params_add('password', required=True, p_type='str', err_msg='')
    param_check.params_add('picture', required=False, p_type='image', err_msg='')
    if register_type == RegisterEnum.user.value:
        flag, cm, msg = param_check.params_parser()
        if not flag:
            return CreateResponse(cm, message=msg).response()
        user_name = param_check.get_argv('user_name')
        password = param_check.get_argv('password')
        picture = param_check.get_argv('picture')
        # 逻辑处理
        kwargs = dict(user_name=user_name, password=password, picture=picture)
        flag, cm, msg = RegisterFactory.deal_with_register(register_type).register(kwargs)
    else:
        param_check.params_add('nick_name', required=True, p_type='str', err_msg='')
        param_check.params_add('phone', required=True, p_type='str', err_msg='')
        param_check.params_add('wechat', required=False, p_type='str', err_msg='')
        param_check.params_add('id_card', required=True, p_type='str', err_msg='')
        param_check.params_add('gender', required=False, p_type='int', err_msg='')
        flag, cm, msg = param_check.params_parser()
        if not flag:
            return CreateResponse(cm, message=msg).response()
        user_name = param_check.get_argv('user_name')
        password = param_check.get_argv('password')
        picture = param_check.get_argv('picture')
        nick_name = param_check.get_argv('nick_name')
        phone = param_check.get_argv('phone')
        wechat = param_check.get_argv('wechat')
        id_card = param_check.get_argv('id_card')
        gender = param_check.get_argv('gender')
        # 逻辑处理
        kwargs = dict(user_name=user_name, password=password, picture=picture, nick_name=nick_name,
                      phone=phone, wechat=wechat, id_card=id_card, gender=gender)
        flag, cm, msg = RegisterFactory.deal_with_register(register_type).register(kwargs)

