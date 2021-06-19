from enum import Enum

class GenderEnum(Enum):
    man = 1
    feman = 2
    unknown = 3

class PermissionEnum(Enum):
    read = 1
    modify = 2
    add = 3
    delete = 4

class RegisterEnum(Enum):
    house_owner = 1
    tenant = 2
    user = 9

if __name__ == "__main__":
    print(RegisterEnum.__dict__.keys())