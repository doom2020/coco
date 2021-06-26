from flaskapp.app_log import LoggerHelp
from flask import Blueprint, send_file, jsonify
from flaskapp.param_check import ParamCheck
from flaskapp.http_response import CodeType, CreateResponse
from flaskapp.settings import *
from flaskapp.v1.models import HouseOwner, Tenant, User
from flaskapp import create_app, log, db
from datetime import datetime


index_bp = Blueprint('index_api', __name__, url_prefix='/api/v1')


@index_bp.route('/', methods=['GET'])
def index_view():
    # 参数校验
    param_check = ParamCheck()
    param_check.params_add('name', required=True, p_type='str', err_msg='')
    param_check.params_add('age', required=True, p_type='int', err_msg='')
    param_check.params_add('height', required=True, p_type='float', err_msg='')
    param_check.params_add('like', required=True, p_type='list', err_msg='')
    param_check.params_add('info', required=True, p_type='dict', err_msg='')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    name = param_check.get_argv('name')
    age = param_check.get_argv('age')
    height = param_check.get_argv('height')
    like = param_check.get_argv('like')
    info = param_check.get_argv('info')
    # 逻辑处理
    ret = dict(name=name, age=age, height=height, like=like, info=info)
    # 正常响应
    return jsonify(ret)


@index_bp.route('/test_img', methods=['GET'])
def test_image():
    img = os.path.join(IMAGE_PATH, 'user', 'u_default.png')
    return send_file(img)


@index_bp.route('/test_add_house_owner', methods=['GET'])
def test_add_house_owner():
    user_name = 'hu'
    nick_name = 'bo'
    password = '123456'
    phone = '13207123556'
    wechat = ''
    id_card = '430333199307015364'
    gender = 'woman'
    picture = '/hu'
    update_time = create_time = datetime.now()
    new_house_owner = HouseOwner(user_name=user_name, nick_name=nick_name, password=password, phone=phone,
                                 wechat=wechat, id_card=id_card, gender=gender, picture=picture,
                                 create_time=create_time, update_time=update_time)
    try:
        db.session.add(new_house_owner)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        log.write(f'<new add failed> - err_info: {e}', level='error')
        return 'error'
    log.write('new add success', level='info')
    return 'success'


@index_bp.route('/test_add_tenant', methods=['GET'])
def test_add_tenant():
    user_name = 'hu'
    nick_name = 'bo'
    password = '123456'
    phone = '13207123556'
    wechat = ''
    id_card = '430333199307015364'
    gender = 'woman'
    picture = '/hu'
    update_time = create_time = datetime.now()
    new_house_owner = Tenant(user_name=user_name, nick_name=nick_name, password=password, phone=phone,
                             wechat=wechat, id_card=id_card, gender=gender, picture=picture,
                             create_time=create_time, update_time=update_time)
    try:
        db.session.add(new_house_owner)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        log.write(f'<new add failed> - err_info: {e}', level='error')
        return 'error'
    log.write('new add success', level='info')
    return 'success'


@index_bp.route('/test_add_user', methods=['GET'])
def test_add_user():
    user_name = 'rui'
    password = '123456'
    picture = '/rui'
    update_time = create_time = datetime.now()
    new_user = User(user_name=user_name, password=password, picture=picture, create_time=create_time,
                    update_time=update_time)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        log.write(f'<new add failed> - err_info: {e}', level='error')
        return 'error'
    log.write('new add success', level='info')
    return 'success'
