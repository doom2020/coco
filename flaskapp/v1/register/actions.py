from abc import ABCMeta, abstractmethod
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
from flaskapp.settings import *
import shutil
from sqlalchemy import and_, or_


class RegisterHandler(metaclass=ABCMeta):
    @abstractmethod
    def register(self, *args, **kwargs):
        pass

    @abstractmethod
    def query(self, **kwargs):
        pass

    @abstractmethod
    def encrypt(self, *args):
        pass

    @abstractmethod
    def add(self, *args):
        pass


class HouseOwnerRegisterHandler(RegisterHandler):
    @staticmethod
    def save_image(img):
        flag, img_name = True, ''
        try:
            img_suffix = img.filename.split('.')[-1]
            now = str(datetime.now())
            img_name = md5(secure_filename(img.filename + now).encode('utf-8')).hexdigest() + '.' + img_suffix
            img.save(os.path.join(HOUSE_OWNER_IMAGE_PATH, img_name))
        except IndexError as e:
            log.write('file name is invalid: %s' % e, level='error')
            flag = False
        except OSError as e:
            log.write('file save failed: %s' % e, level='error')
            flag = False
        return flag, img_name

    @staticmethod
    def remove_image(img):
        flag = True
        try:
            shutil.rmtree(img)
        except OSError as e:
            log.write('remove file failed: %s' % e, level='error')
            flag = False
        return flag

    def query(self, **kwargs):
        objs = MysqlQuery.query_filter(**kwargs)
        return objs

    def encrypt(self, password):
        return Tools.encrypt_str(password)

    def add(self, user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture, create_time, update_time):
        flag, img_name = self.save_image(picture)
        if not flag:
            return False, CodeType.IMAGE_SAVE_FAILED, ''
        img_url = f'{HTTP_PROTOCOL}://{REMOTE_SERVER_IP}:{SERVER_PORT}/api/v1/get_house_owner_img/{img_name}'
        new_house_owner = HouseOwner(user_name=user_name, nick_name=nick_name, password=encrypt_pwd, phone=phone,
                                     wechat=wechat, id_card=id_card, gender=gender, picture=img_url,
                                     create_time=create_time, update_time=update_time)
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
        # ????????????
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        nick_name = kwargs['nick_name']
        phone = kwargs['phone']
        wechat = kwargs['wechat']
        id_card = kwargs['id_card']
        gender = kwargs['gender']
        update_time = create_time = datetime.now()
        # ???????????????`nick_name`, `phone`, `id_card`??????????????????,??????????????????
        filter_condition = {
            and_(
                and_(
                    HouseOwner.is_delete == 0,
                ),
                or_(
                    HouseOwner.nick_name == nick_name,
                    HouseOwner.phone == phone,
                    HouseOwner.id_card == id_card
                )
            )
        }
        objs = self.query(**dict(db_model=HouseOwner, query_type='all', filter_condition=filter_condition))
        if objs:
            return False, CodeType.DATABASE_QUERY_EXIST, ''
        # ??????????????????
        flag, ret, msg = self.encrypt(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        # ????????????
        flag, ret, msg = self.add(user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture,
                                  create_time, update_time)
        return flag, ret, msg
        

class TenantRegisterHandler(RegisterHandler):
    @staticmethod
    def save_image(img):
        flag, img_name = True, ''
        try:
            img_suffix = img.filename.split('.')[-1]
            now = str(datetime.now())
            img_name = md5(secure_filename(img.filename + now).encode('utf-8')).hexdigest() + '.' + img_suffix
            img.save(os.path.join(TENANT_IMAGE_PATH, img_name))
        except IndexError as e:
            log.write('file name is invalid: %s' % e, level='error')
            flag = False
        except OSError as e:
            log.write('file save failed: %s' % e, level='error')
            flag = False
        return flag, img_name

    @staticmethod
    def remove_image(img):
        flag = True
        try:
            shutil.rmtree(img)
        except OSError as e:
            log.write('remove file failed: %s' % e, level='error')
            flag = False
        return flag

    def query(self, **kwargs):
        objs = MysqlQuery.query_filter(**kwargs)
        return objs

    def encrypt(self, password):
        return Tools.encrypt_str(password)

    def add(self, user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture, create_time, update_time):
        flag, img_name = self.save_image(picture)
        if not flag:
            return False, CodeType.IMAGE_SAVE_FAILED, ''
        img_url = f'{HTTP_PROTOCOL}://{REMOTE_SERVER_IP}:{SERVER_PORT}/api/v1/get_tenant_img/{img_name}'
        new_tenant = Tenant(user_name=user_name, nick_name=nick_name, password=encrypt_pwd, phone=phone, wechat=wechat,
                            id_card=id_card, gender=gender, picture=img_url, create_time=create_time,
                            update_time=update_time)
        try:
            db.session.add(new_tenant)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            log.write(f'<add new_tenant failed> - err_info: {e}', level='error')
            return False, CodeType.DATABASE_ADD_ERROR, 'add new_tenant failed'
        log.write('add new_tenant success', level='info')
        return True, CodeType.SUCCESS_RESPONSE, ''

    def register(self, **kwargs):
        # ????????????
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        nick_name = kwargs['nick_name']
        phone = kwargs['phone']
        wechat = kwargs['wechat']
        id_card = kwargs['id_card']
        gender = kwargs['gender']
        update_time = create_time = datetime.now()
        # ???????????????`nick_name`, `phone`, `id_card`??????????????????,??????????????????
        filter_condition = {
            and_(
                and_(
                    Tenant.is_delete == 0,
                ),
                or_(
                    Tenant.nick_name == nick_name,
                    Tenant.phone == phone,
                    Tenant.id_card == id_card
                )
            )
        }
        objs = self.query(**dict(db_model=Tenant, query_type='all', filter_condition=filter_condition))
        if objs:
            return False, CodeType.DATABASE_QUERY_EXIST, ''
        # ??????????????????
        flag, ret, msg = self.encrypt(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        # ????????????
        flag, ret, msg = self.add(user_name, nick_name, encrypt_pwd, phone, wechat, id_card, gender, picture,
                                  create_time, update_time)
        return flag, ret, msg


class UserRegisterHandler(RegisterHandler):
    @staticmethod
    def save_image(img):
        flag, img_name = True, ''
        try:
            img_suffix = img.filename.split('.')[-1]
            now = str(datetime.now())
            img_name = md5(secure_filename(img.filename + now).encode('utf-8')).hexdigest() + '.' + img_suffix
            img.save(os.path.join(USER_IMAGE_PATH, img_name))
        except IndexError as e:
            log.write('file name is invalid: %s' % e, level='error')
            flag = False
        except OSError as e:
            log.write('file save failed: %s' % e, level='error')
            flag = False
        return flag, img_name

    @staticmethod
    def remove_image(img):
        flag = True
        try:
            shutil.rmtree(img)
        except OSError as e:
            log.write('remove file failed: %s' % e, level='error')
            flag = False
        return flag

    def query(self, **kwargs):
        objs = MysqlQuery.query_filter(**kwargs)
        return objs

    def encrypt(self, password):
        return Tools.encrypt_str(password)

    def add(self, user_name, encrypt_pwd, picture, create_time, update_time):
        flag, img_name = self.save_image(picture)
        if not flag:
            return False, CodeType.IMAGE_SAVE_FAILED, ''
        img_url = f'{HTTP_PROTOCOL}://{REMOTE_SERVER_IP}:{SERVER_PORT}/api/v1/get_user_img/{img_name}'
        new_user = User(user_name=user_name, password=encrypt_pwd, picture=img_url, create_time=create_time,
                        update_time=update_time)
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

    # ????????????
    def register(self, **kwargs):
        user_name = kwargs['user_name']
        password = kwargs['password']
        picture = kwargs['picture']
        update_time = create_time = datetime.now()
        # ???????????????`user_name`??????????????????,??????????????????
        filter_condition = {
            and_(
                User.user_name == user_name,
                User.is_delete == 0
            )
        }
        objs = self.query(**dict(db_model=User, query_type='all', filter_condition=filter_condition))
        if objs:
            return False, CodeType.DATABASE_QUERY_EXIST, ''
        # ??????????????????
        flag, ret, msg = self.encrypt(password)
        if not flag:
            return flag, ret, msg
        else:
            encrypt_pwd = ret
        # ????????????
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
