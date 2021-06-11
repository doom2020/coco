from flask import Flask
from flaskapp import config
from flaskapp.app_log import LoggerHelp

# 初始化日志实例 
log = LoggerHelp()

def create_app(debug_mode=False):
    app = Flask(__name__)
    if debug_mode:
        # 加载debug模式配置信息
        app.config.from_object(config.DevelopmentConfig)
    else:
        # 加载非debug模式配置信息
        app.config.from_object(config.ProductionConfig)
    # 导入视图
    from flaskapp.v1.index import views
    # 注册蓝图
    app.register_blueprint(views.index_bp)
    log.write('app is run', level='exception')
    return app
    