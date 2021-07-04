from abc import ABCMeta, abstractmethod
from flaskapp.enumeration import *


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

    def login_by_phone(self, *args, **kwargs):
        phone = kwargs['phone']
        auth_code = kwargs['auth_code']
        check_code = kwargs['check_code']


class TenantLoginHandler(LoginHandler):
    def login_by_account(self, *args, **kwargs):
        nick_name = kwargs['nick_name']
        password = kwargs['password']
        check_code = kwargs['check_code']

    def login_by_phone(self, *args, **kwargs):
        phone = kwargs['phone']
        auth_code = kwargs['auth_code']
        check_code = kwargs['check_code']


class UserLoginHandler(LoginHandler):
    def login_by_account(self, *args, **kwargs):
        nick_name = kwargs['nick_name']
        password = kwargs['password']
        check_code = kwargs['check_code']

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


