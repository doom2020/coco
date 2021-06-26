from enum import Enum


class GenderEnum(Enum):
    man = 'man'
    woman = 'woman'
    unknown = 'unknown'


class PermissionEnum(Enum):
    read = 'read'
    modify = 'modify'
    add = 'add'
    delete = 'delete'


class RegisterEnum(Enum):
    house_owner = 'house_owner'
    tenant = 'tenant'
    user = 'user'


if __name__ == "__main__":
    print(RegisterEnum.__dict__.keys())