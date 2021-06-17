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