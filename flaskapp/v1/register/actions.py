from abc import ABCMeta, abstractmethod
from sys import argv
import flaskapp
from flaskapp.http_response import CodeType
from flaskapp.tools import Tools
from flaskapp.mysql_query import MysqlQuery
from flaskapp.v1.models import HouseOwner, Tenant, User
from flaskapp.enumeration import RegisterEnum
from datetime import datetime
from flaskapp import log
from flaskapp import db
from hashlib import md5
from werkzeug.utils import secure_filename
import os
from flaskapp.settings import *
import shutil


class RegisterHandler(metaclass=ABCMeta):
    @abstractmethod
    def register(self, *args, **kwargs):
        pass

    @abstractmethod
    def query(self, *args, **kwargs):
        pass

    @abstractmethod
    def encrypt(self, *args, **kwargs):
        pass

    @abstractmethod
    def add(self, *args, **kwargs):
        pass


class HouseOwnerRegisterHandler(RegisterHandler):
    def query(self, *args, **kwargs):
        objs = MysqlQuery.query_filter(*args, **kwargs)
        return objs

    def encrypt(self, *args, **kwargs):
        return Tools.encrypt_str(args[0])

    def add(self, *args, **kwargs):
        new_house_owner = HouseOwner(user_name=args[0], nick_name=args[1], password=args[2], phone=args[3],
                                     wechat=args[4], id_card=args[5], gender=args[6], picture=args[7],
                                     create_time=args[8], update_time=args[9])
        try:
            db.session.add(new_house_owner)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            log.write(f'<add new_house_owner failed> - err_info: {e}', level='error')
            return False, CodeType.DATABASE_ADD_ERROR, 'add new_house_owner failed'
        log.write('add new_house_owner success', level='info')
        return True, CodeType.SUCCESS_RESPONSE, ''

    def register(self, *args, **kwargs):
        # 参数获取
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        nick_name = kwargs['nick_name']
        phone = kwargs['phone']
        wechat = kwargs['wechat']
        id_card = kwargs['id_card']
        gender = kwargs['gender']
        update_time = create_time = datetime.now()
        # 数据库查询`nick_name`, `phone`, `id_card`是否已经存在
        and_filter_condition = dict(nick_name=nick_name, phone=phone, id_card=id_card, is_delete=False)
        objs = self.query(HouseOwner, **dict(and_filter_condition=and_filter_condition))
        if objs:
            return False, CodeType.DATABASE_QUERY_EXIST, ''
        # 进行密码加密
        flag, ret, msg = self.encrypt(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        # 数据写入
        flag, ret, msg = self.add(user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture,
                                  create_time, update_time)
        return flag, ret, msg
        

class TenantRegisterHandler(RegisterHandler):
    def query(self, *args, **kwargs):
        objs = MysqlQuery.query_filter(*args, **kwargs)
        return objs

    def encrypt(self, *args, **kwargs):
        return Tools.encrypt_str(args[0])

    def add(self, *args, **kwargs):
        new_tenant = Tenant(user_name=args[0], nick_name=args[1], password=args[2], phone=args[3],
                            wechat=args[4], id_card=args[5], gender=args[6], picture=args[7],
                            create_time=args[8], update_time=args[9])
        try:
            db.session.add(new_tenant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            log.write(f'<add new_tenant failed> - err_info: {e}', level='error')
            return False, CodeType.DATABASE_ADD_ERROR, 'add new_tenant failed'
        log.write('add new_tenant success', level='info')
        return True, CodeType.SUCCESS_RESPONSE, ''

    def register(self, *args, **kwargs):
        # 参数获取
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        nick_name = kwargs['nick_name']
        phone = kwargs['phone']
        wechat = kwargs['wechat']
        id_card = kwargs['id_card']
        gender = kwargs['gender']
        update_time = create_time = datetime.now()
        # 数据库查询`nick_name`, `phone`, `id_card`是否已经存在
        and_filter_condition = dict(nick_name=nick_name, phone=phone, id_card=id_card, is_delete=False)
        objs = self.query(Tenant, **dict(and_filter_condition=and_filter_condition))
        if objs:
            return False, CodeType.DATABASE_QUERY_EXIST, ''
        # 进行密码加密
        flag, ret, msg = self.encrypt(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        # 数据写入
        flag, ret, msg = self.add(user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture,
                                  create_time, update_time)
        return flag, ret, msg


class UserRegisterHandler(RegisterHandler):
    def save_image(img):
        flag, img_name = True, ''
        try:
            img_suffix = img.filename.split('.')[-1]
            now = str(datetime.now())
            img_name = md5(secure_filename(img.filename + now).encode('utf-8')).hexdigest() + '.' + img_suffix
            img.save(os.path.join(USER_IMAGE_PATH, img_name))
        except Exception as e:
            flag = False
        return flag, img_name
    
    def remove_image(img):
        flag = True
        try:
            shutil.rmtree(img)
        except Exception as e:
            flag = False
        return flag

    def query(self, *args, **kwargs):
        objs = MysqlQuery.query_filter(*args, **kwargs)
        return objs

    def encrypt(self, *args, **kwargs):
        return Tools.encrypt_str(args[0])

    def add(self, *args, **kwargs):
        img = args[2]
        flag, img_name = self.save_image(img)
        if not flag:
            return False, CodeType.IMAGE_SAVE_FAILED, ''
        img_url = f'http://127.0.0.1:{SERVER_PORT}/api/v1/get_user_img/{img_name}'
        new_user = User(user_name=args[0], password=args[1], picture=img_url, create_time=args[3], update_time=args[4])
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            log.write(f'<add new_user failed> - err_info: {e}', level='error')
            img = os.path.join(USER_IMAGE_PATH, img_name)
            flag = self.remove_image(img)
            if not flag:
                log.write('remove image failed', level='error')
            return False, CodeType.DATABASE_ADD_ERROR, 'add new_user failed'
        log.write('add new_user success', level='info')
        return True, CodeType.SUCCESS_RESPONSE, ''

    # 参数获取
    def register(self, *args, **kwargs):
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        update_time = create_time = datetime.now()
        # 数据库查询`user_name`是否已经存在
        and_filter_condition = dict(user_name=user_name, is_delete=False)
        objs = self.query(User, **dict(and_filter_condition=and_filter_condition))
        if objs:
            return False, CodeType.DATABASE_QUERY_EXIST, ''
        # 进行密码加密
        flag, ret, msg = self.encrypt(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        # 数据写入
        flag, ret, msg = self.add(user_name, encrypt_pwd, picture, create_time, update_time)
        return flag, ret, msg


class RegisterFactory(object):
    @classmethod
    def deal_with_register(cls, register_type):
        if register_type == RegisterEnum.house_owner.value:
            return HouseOwnerRegisterHandler()
        elif register_type == RegisterEnum.tenant.value:
            return TenantRegisterHandler()
        elif register_type == RegisterEnum.user.value:
            return UserRegisterHandler()
