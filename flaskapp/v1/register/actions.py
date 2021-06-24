from abc import ABCMeta, abstractmethod
from flaskapp.v1.models import HouseOwner, User
from flaskapp.enumeration import RegisterEnum


class RegisterHandler(metaclass=ABCMeta):
    @abstractmethod
    def register(self, *args, **kwargs):
        pass


class HouseOwnerRegisterHandler(RegisterHandler):
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


class TenantRegisterHandler(RegisterHandler):
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


class UserRegisterHandler(RegisterHandler):
    # 参数获取
    def register(self, *args, **kwargs):
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']

        User.query.all()

class RegisterFactory(object):
    @classmethod
    def deal_with_register(cls, register_type):
        if register_type == RegisterEnum.house_owner.value:
            return HouseOwnerRegisterHandler()
        elif register_type == RegisterEnum.tenant.value:
            return TenantRegisterHandler()
        elif register_type == RegisterEnum.user.value:
            return UserRegisterHandler()