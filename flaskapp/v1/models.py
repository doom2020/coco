from flaskapp import db
from flaskapp.enumeration import GenderEnum, PermissionEnum


class HouseOwner(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'house_owner'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=False, nullable=False)
    nick_name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(2048), nullable=False)
    phone = db.Column(db.String(32), unique=True, nullable=False, index=True)
    wechat = db.Column(db.String(128), unique=True, nullable=True, default='')
    id_card = db.Column(db.String(64), unique=True, nullable=False, index=True)
    gender = db.Column(db.Enum(GenderEnum), nullable=False, default=1)
    score = db.Column(db.DECIMAL(5, 2), nullable=False, default=100.00)
    picture = db.Column(db.String(64), unique=False, nullable=False, default='/')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.nick_name


class Tenant(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'tenant'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=False)
    nick_name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(2048), nullable=False)
    phone = db.Column(db.String(32), unique=True, nullable=False, index=True)
    wechat = db.Column(db.String(128), unique=True, nullable=True, default='')
    id_card = db.Column(db.String(64), unique=True, nullable=False, index=True)
    gender = db.Column(db.Enum(GenderEnum), nullable=False, default=1)
    score = db.Column(db.DECIMAL(5, 2), nullable=False, default=100.00)
    picture = db.Column(db.String(64), unique=False, nullable=False, default='/')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.nick_name

class User(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(2048), nullable=False)
    picture = db.Column(db.String(64), unique=False, nullable=False, default='/')
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.user_name


class Role(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), unique=True, index=True)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.role_name


class Menu(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'Menu'
    id = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(32))
    permission = db.Column(db.Enum(PermissionEnum), nullable=False, default=1)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.menu_name

class UserRole(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    role_id = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.id

class RoleMenu(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'role_menu'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, nullable=False)
    menu_id = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean(), nullable=False, default=0)

    @classmethod
    def to_dict(cls):
        ret_dict = dict()
        for key, value in cls.__dict__.items():
            if '__' not in key and key != 'to_dict':
                ret_dict[key] = value
        return ret_dict

    def __str__(self):
        return self.id









    