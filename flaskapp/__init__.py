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
    from flaskapp.v1.models import HouseOwner, Tenant, User, Role, Menu, UserRole, RoleMenu
    db.init_app(app)
    # 创建表or删除表
    with app.app_context():
        pass
        # 创建所有
        # db.create_all()
        # 删除所有
        # db.drop_all()
        # 创建指定表
        # db.create_all(bind=['users'])
    # 导入视图
    from flaskapp.v1.index import views
    # 注册蓝图
    app.register_blueprint(views.index_bp)
    log.write('App is running', level='info')
    return app


def create_all_table():
    db.create_all(bind='__all__')


def drop_all_table():
    db.drop_all(bind='__all__')


def create_target_table(database_names=[]):
    db.create_all(bind=database_names)


def drop_target_table(database_names=[]):
    db.drop_all(bind=database_names)
