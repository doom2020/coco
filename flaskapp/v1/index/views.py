from flask import Blueprint, send_file
from flask.json import jsonify
from flaskapp.param_check import ParamCheck
from flaskapp.http_response import CreateResponse
from flaskapp.settings import *


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


@index_bp.route('/get_img', methods=['GET'])
def image_test():
    img = os.path.join(IMAGE_PATH, 'user', 'u_default.png')
    return send_file(img)
