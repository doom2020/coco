from flask import Flask
from flaskapp import config
from flaskapp.app_log import LoggerHelp
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy

# 初始化日志实例 
log = LoggerHelp()

db = SQLAlchemy()

def create_app(debug_mode=False):
    app = Flask(__name__)
    if debug_mode:
        # 加载debug模式配置信息
        app.config.from_object(config.DevelopmentConfig)
    else:
        # 加载非debug模式配置信息
        app.config.from_object(config.ProductionConfig)
    
    # 初始化
    db.init_app(app)
    with app.app_context():
        db.create_all(bind='users')
    # 导入视图
    from flaskapp.v1.index import views
    # 注册蓝图
    app.register_blueprint(views.index_bp)
    log.write('App is running', level='info')
    return app
    