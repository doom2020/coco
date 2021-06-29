from werkzeug.utils import secure_filename
from flask import request
from flaskapp import param_check
from flaskapp.enumeration import GenderEnum, PermissionEnum, RegisterEnum
from flaskapp.app_log import LoggerHelp
from flask import Blueprint, send_file, jsonify
from flaskapp.param_check import ParamCheck
from flaskapp.http_response import CodeType, CreateResponse
from flaskapp.settings import *
from flaskapp.v1.models import HouseOwner, Tenant, User
from flaskapp import create_app, log, db
from datetime import datetime
from hashlib import md5


index_bp = Blueprint('index_api', __name__, url_prefix='/api/v1')


"""*****************功能测试api接口**********************"""


# 首页请求测试
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


"""****************图片测试api接口**********************"""


@index_bp.route('/test_img', methods=['GET'])
def test_image():
    img = os.path.join(IMAGE_PATH, 'user', 'u_default.png')
    return send_file(img)


img_format = 'http://127.0.0.1:5000/api/v1/get_user_img/u_default'


@index_bp.route('/get_house_owner_img/<string:img_name>')
def get_house_owner_img(img_name):
    img = os.path.join(HOUSE_OWNER_IMAGE_PATH, img_name + '.png')
    if not os.path.exists(img):
        return CreateResponse(CodeType.IMAGE_FILE_IS_NOT_EXIST, message=f'the img: {img} is not exist').response()
    return send_file(img)


@index_bp.route('/get_house_owner_img/<string:img_name>')
def get_tenant_img(img_name):
    img = os.path.join(TENANT_IMAGE_PATH, img_name + '.png')
    if not os.path.exists(img):
        return CreateResponse(CodeType.IMAGE_FILE_IS_NOT_EXIST, message=f'the img: {img} is not exist').response()
    return send_file(img)


@index_bp.route('/get_user_img/<string:img_name>')
def get_user_img(img_name):
    img = os.path.join(USER_IMAGE_PATH, img_name + '.png')
    if not os.path.exists(img):
        return CreateResponse(CodeType.IMAGE_FILE_IS_NOT_EXIST, message=f'the img: {img} is not exist').response()
    return send_file(img)


"""*******************注册功能api接口测试**************************"""


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


"""***********************通用枚举值api接口**************************"""


@index_bp.route('/get_permission_types', methods=['GET'])
def get_permisson_types():
    permission_set = set()
    for key in PermissionEnum.__dict__.keys():
        if not key.startswith('_'):
            permission_set.add(key)
    result = dict(permission_set=str(permission_set))
    return CreateResponse(CodeType.SUCCESS_RESPONSE, result=result).response()


@index_bp.route('/get_gender_types', methods=['GET'])
def get_gender_types():
    gender_set = set()
    for key in GenderEnum.__dict__.keys():
        if not key.startswith('_'):
            gender_set.add(key)
    result = dict(gender_set=str(gender_set))
    return CreateResponse(CodeType.SUCCESS_RESPONSE, result=result).response()


@index_bp.route('/get_register_types', methods=['GET'])
def get_register_types():
    register_set = set()
    for key in RegisterEnum.__dict__.keys():
        if not key.startswith('_'):
            register_set.add(key)
    result = dict(register_set=str(register_set))
    return CreateResponse(CodeType.SUCCESS_RESPONSE, result=result).response()


# 图片上传测试
@index_bp.route('/upload_image', methods=['POST'])
def upload_image():
    param_check = ParamCheck()
    param_check.params_add('image', required=True, p_type='image',err_msg='')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    img = param_check.parser_args.get('image')
    img_suffix = img.filename.split('.')[-1]
    now = str(datetime.now())
    img_name = md5(secure_filename(img.filename + now).encode('utf-8')).hexdigest() + '.' + img_suffix
    img.save(os.path.join(USER_IMAGE_PATH, img_name))
    return img_name


# 文件上传测试
@index_bp.route('/upload_file', methods=['POST'])
def upload_file():
    param_check = ParamCheck()
    param_check.params_add('file', required=True, p_type='file', err_msg='')
    flag, cm, msg = param_check.params_parser()
    if not flag:
        return CreateResponse(cm, message=msg).response()
    file = param_check.parser_args.get('file')
    file_suffix = file.filename.split('.')[-1]
    now = str(datetime.now())
    file_name = md5(secure_filename(file.filename + now).encode('utf-8')).hexdigest() + '.' + file_suffix
    file.save(os.path.join(FILE_PATH, file_name))
    return file_name


# content_type测试
@index_bp.route('/get_data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        name = request.args.get('name', '')
        age = request.values.get('age', 3)
        print(name)
        print(age)
        return jsonify(name=name, age=age)
    if request.method == 'POST':
        name = request.form.get('name', '')
        age = request.values.get('age', '')
        print(name)
        print(age)
        return jsonify(name=name, age=age)


@index_bp.before_request
def get_content_type():
    print(request.content_type)

