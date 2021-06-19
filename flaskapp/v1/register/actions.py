from abc import ABCMeta, abstractmethod

class RegisterHandler(ABCMeta):
    def __init__(self, register_type=None):
        self.register_type = register_type


class HouseOwnerRegisterHandler(RegisterHandler):
    pass


class TenantRegisterHandler(RegisterHandler):
    pass


class UserRegisterHandler(RegisterHandler):
    pass