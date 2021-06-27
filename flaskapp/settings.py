"""
通用配置信息(除flask内置配置)
"""
import os

# 是否启用调试模式(生产环境关闭debug模式)
DEBUG_MODE = True

# 日志目录
LOG_PATH = os.getcwd() if DEBUG_MODE else '/var/applog'
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
# 日志文件
LOG_FILE = os.path.join(LOG_PATH, 'flaskapp.log')

# 服务ip地址
SERVER_IP = '0.0.0.0'
# 服务端口
SERVER_PORT = 5000 if DEBUG_MODE else 8000

# 图片目录
IMAGE_PATH = os.path.join(os.getcwd(), 'flaskapp', 'static', 'image') if DEBUG_MODE else '/var/image'
if not os.path.exists(IMAGE_PATH):
    os.makedirs(IMAGE_PATH)
# house_owner 图片目录
HOUSE_OWNER_IMAGE_PATH = os.path.join(IMAGE_PATH, 'house_owner')
if not os.path.exists(HOUSE_OWNER_IMAGE_PATH):
    os.makedirs(HOUSE_OWNER_IMAGE_PATH)
# tenant 图片目录
TENANT_IMAGE_PATH = os.path.join(IMAGE_PATH, 'tenant')
if not os.path.exists(TENANT_IMAGE_PATH):
    os.makedirs(TENANT_IMAGE_PATH)
# user 图片目录
USER_IMAGE_PATH = os.path.join(IMAGE_PATH, 'user')
if not os.path.exists(USER_IMAGE_PATH):
    os.makedirs(USER_IMAGE_PATH)

# 文件目录
FILE_PATH = os.path.join(os.getcwd(), 'flaskapp', 'static', 'files') if DEBUG_MODE else '/var/files'
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)

# 加密的秘钥
ENCRYPT_KEY = '-9=-6fhbcmzsawt$#jnd897*()&^%hjfnvf>'

# 允许的文件拓展名
ALLOW_FILE_EXTENSIONS = {'txt', 'pdf', 'csv', 'xml', 'png', 'jpg', 'jpeg', 'gif'}

# 允许的图片拓展名
ALLOW_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



