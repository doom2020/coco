"""
通用配置信息(除flask内置配置)
"""
import os

# 是否启用调试模式(生产环境关闭debug模式)
DEBUG_MODE = True

LOG_PATH = os.getcwd() if DEBUG_MODE else '/var/applog'
LOG_FILE = os.path.join(LOG_PATH, 'flaskapp.log')

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5000 if DEBUG_MODE else 8000

IMAGE_PATH = os.path.join(os.getcwd(), 'flaskapp', 'static', 'image') if DEBUG_MODE else '/var/image'


