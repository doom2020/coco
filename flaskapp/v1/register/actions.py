from abc import ABCMeta, abstractmethod
import flaskapp
from flaskapp.http_response import CodeType
from flaskapp.tools import Tools
from flaskapp.mysql_query import MysqlQuery
from flaskapp.v1.models import HouseOwner, Tenant, User
from flaskapp.enumeration import RegisterEnum
from datetime import datetime
from flaskapp import log
from flaskapp import db


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
        flag, ret = False, False
        return flag, ret

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
        flag, ret = self.query(nick_name, phone, id_card)
        if not flag:
            return flag, ret
        # 进行密码加密
        flag, ret = self.encrypt(password)
        if not flag:
            return flag, ret
        else:
            encrypt_pwd = ret
        # 数据写入
        flag, ret, msg = self.add(user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture,
                                  create_time, update_time)
        return flag, ret, msg
        

class TenantRegisterHandler(RegisterHandler):
    def query(self, *args, **kwargs):
        pass
        flag, ret = True, True
        return flag, ret

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
        flag, ret = self.query(nick_name, phone, id_card)
        if not flag:
            return flag, ret
        # 进行密码加密
        flag, ret = self.encrypt(password)
        if not flag:
            return flag, ret
        else:
            encrypt_pwd = ret
        # 数据写入
        flag, ret, msg = self.add(user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture,
                                  create_time, update_time)
        return flag, ret


class UserRegisterHandler(RegisterHandler):
    def query(self, *args, **kwargs):
        pass
        flag, ret = True, True
        return flag, ret

    def encrypt(self, *args, **kwargs):
        return Tools.encrypt_str(args[0])

    def add(self, *args, **kwargs):
        new_user = User(user_name=args[0], password=args[1], picture=args[2], create_time=args[3], update_time=args[4])
        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            log.write(f'<add new_user failed> - err_info: {e}', level='error')
            return False, CodeType.DATABASE_ADD_ERROR, 'add new_user failed'
        log.write('add new_user success', level='info')
        return True, CodeType.SUCCESS_RESPONSE, ''

    # 参数获取
    def register(self, *args, **kwargs):
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        update_time = create_time = datetime.now()
        # 数据库查询`nick_name`, `phone`, `id_card`是否已经存在
        flag, ret = self.query(user_name)
        if not flag:
            return flag, ret
        # 进行密码加密
        flag, ret = self.encrypt(password)
        if not flag:
            return flag, ret
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
