from abc import ABCMeta, abstractmethod
from flaskapp.enumeration import *
from flaskapp.v1.models import *
from flaskapp.tools import *
from flaskapp.mysql_query import *
from flaskapp.http_response import *


class LoginHandler(metaclass=ABCMeta):
    @abstractmethod
    def login_by_account(self, *args, **kwargs):
        pass

    @abstractmethod
    def login_by_phone(self, *args, **kwargs):
        pass


class HouseOwnerLoginHandler(LoginHandler):
    def login_by_account(self, *args, **kwargs):
        nick_name = kwargs['nick_name']
        password = kwargs['password']
        check_code = kwargs['check_code']
        if not check_code:
            # 验证码后面优化逻辑
            return False, CodeType.CODE_IS_ERROR, ''
        flag, ret, msg = Tools.encrypt_str(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        filter_condition = {
            and_(
                HouseOwner.nick_name == nick_name,
                HouseOwner.password == encrypt_pwd
            )
        }
        objs = MysqlQuery.query_filter(**dict(db_model=HouseOwner, query_type='all', filter_condition=filter_condition))
        if not objs:
            return False, CodeType.DATABASE_QUERY_BLANK, ''
        elif len(objs) != 1:
            return False, CodeType.DATABASE_QUERY_MANY, ''

    def login_by_phone(self, *args, **kwargs):
        phone = kwargs['phone']
        auth_code = kwargs['auth_code']
        check_code = kwargs['check_code']
        pass


class TenantLoginHandler(LoginHandler):
    def login_by_account(self, *args, **kwargs):
        nick_name = kwargs['nick_name']
        password = kwargs['password']
        check_code = kwargs['check_code']
        if not check_code:
            # 验证码后面优化逻辑
            return False, CodeType.CODE_IS_ERROR, ''
        flag, ret, msg = Tools.encrypt_str(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        filter_condition = {
            and_(
                Tenant.nick_name == nick_name,
                Tenant.password == encrypt_pwd
            )
        }
        objs = MysqlQuery.query_filter(**dict(db_model=Tenant, query_type='all', filter_condition=filter_condition))
        if not objs:
            return False, CodeType.DATABASE_QUERY_BLANK, ''
        elif len(objs) != 1:
            return False, CodeType.DATABASE_QUERY_MANY, ''

    def login_by_phone(self, *args, **kwargs):
        phone = kwargs['phone']
        auth_code = kwargs['auth_code']
        check_code = kwargs['check_code']
        pass


class UserLoginHandler(LoginHandler):
    def login_by_account(self, *args, **kwargs):
        user_name = kwargs['user_name']
        password = kwargs['password']
        check_code = kwargs['check_code']
        if not check_code:
            # 验证码后面优化逻辑
            return False, CodeType.CODE_IS_ERROR, ''
        flag, ret, msg = Tools.encrypt_str(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        filter_condition = {
            and_(
                User.user_name == user_name,
                User.password == encrypt_pwd
            )
        }
        objs = MysqlQuery.query_filter(**dict(db_model=User, query_type='all', filter_condition=filter_condition))
        if not objs:
            return False, CodeType.DATABASE_QUERY_BLANK, ''
        elif len(objs) != 1:
            return False, CodeType.DATABASE_QUERY_MANY, ''

    def login_by_phone(self, *args, **kwargs):
        pass


class LoginFactory(object):
    @classmethod
    def deal_with_login(cls, login_type):
        if login_type == RegisterEnum.house_owner.value:
            return HouseOwnerLoginHandler()
        elif login_type == RegisterEnum.tenant.value:
            return TenantLoginHandler()
        elif login_type == RegisterEnum.user.value:
            return UserLoginHandler()


