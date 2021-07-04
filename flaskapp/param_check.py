from flaskapp.settings import ALLOW_FILE_EXTENSIONS, ALLOW_IMAGE_EXTENSIONS
from flask import request
from flaskapp.http_response import CodeType
import ast
import traceback
from flaskapp.enumeration import *


class ParamCheck(object):
    def __init__(self):
        self.args = []
        self.parser_args = {}
        self.all_params_valid = True
        self.content_type = request.content_type
    
    def get_argv_by_content_type(self, param):
        if self.content_type == 'application/json':
            argv = request.get_json(silent=True).get(param, '')
        elif 'multipart/form-data' in self.content_type:
            argv = request.form.get(param, '')
        else:
            argv = request.values.get(param, '')
        return argv

    def check_str(self, argv_info):
        """
        字符串类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = self.get_argv_by_content_type(param)
        # argv = request.values.get(param)
        # argv = request.form[param]
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, str):
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_STR_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_STR_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def check_int(self, argv_info):
        """
        整数类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = self.get_argv_by_content_type(param)
        # argv = request.values.get(param)
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, int):
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_INT_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, int):
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_INT_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def check_float(self, argv_info):
        """
        浮点类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = self.get_argv_by_content_type(param)
        # argv = request.values.get(param)
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, float):
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_FLOAT_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, float):
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_FLOAT_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def check_list(self, argv_info):
        """
        列表类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = self.get_argv_by_content_type(param)
        # argv = request.values.get(param)
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            try:
                argv = ast.literal_eval(argv)
            except Exception as e:
                print(traceback.format_exc(limit=1))
                self.all_params_valid = False
                return False, CodeType.ARGV_LIST_INVALID_ERROR, err_msg
            if not isinstance(argv, list):
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_LIST_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, list):
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_LIST_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def check_dict(self, argv_info):
        """
        字典类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = self.get_argv_by_content_type(param)
        # argv = request.values.get(param)
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            try:
                argv = ast.literal_eval(argv)
            except Exception as e:
                print(traceback.format_exc(limit=1))
                self.all_params_valid = False
                return False, CodeType.ARGV_DICT_INVALID_ERROR, err_msg
            if not isinstance(argv, dict):
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_DICT_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, dict):
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_DICT_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def check_image(self, argv_info):
        """
        图片校验(待完成)
        """
        param, required, p_type, err_msg = argv_info
        argv = request.files.get(param, '')
        try:
            file_name = argv.filename
        except AttributeError as e:
            if not err_msg:
                err_msg = f'the argv: {param} is not file'
            return False, CodeType.ARGV_IS_NOT_FILE, err_msg
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            if file_name.split('.')[-1] not in ALLOW_IMAGE_EXTENSIONS:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_IMAGE_TYPE_ERROR, err_msg
        else:
            if argv:
                if file_name.split('.')[-1] not in ALLOW_IMAGE_EXTENSIONS:
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_IMAGE_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def check_file(self, argv_info):
        """
        文件校验(待完成)
        """
        param, required, p_type, err_msg = argv_info
        argv = request.files.get(param, '')
        try:
            file_name = argv.filename
        except AttributeError as e:
            if not err_msg:
                err_msg = f'the argv: {param} is not file'
            return False, CodeType.ARGV_IS_NOT_FILE, err_msg
        if required:
            if not argv:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} is blank'
                return False, CodeType.ARGV_IS_BLANK, err_msg
            if file_name.split('.')[-1] not in ALLOW_FILE_EXTENSIONS:
                self.all_params_valid = False
                if not err_msg:
                    err_msg = f'the argv: {param} type is error'
                return False, CodeType.ARGV_FILE_TYPE_ERROR, err_msg
        else:
            if argv:
                if file_name.split('.')[-1] not in ALLOW_FILE_EXTENSIONS:
                    self.all_params_valid = False
                    if not err_msg:
                        err_msg = f'the argv: {param} type is error'
                    return False, CodeType.ARGV_FILE_TYPE_ERROR, err_msg
        self.parser_args[param] = argv
        return True, '', ''

    def params_add(self, param, required=False, p_type=None, err_msg=''):
        self.args.append((param, required, p_type, err_msg))

    def params_parser(self):
        cm, msg = None, None
        if self.args:
            for _ in range(len(self.args)):
                argv_info = self.args.pop()
                if argv_info[2] == 'str':
                    flag, cm, msg = self.check_str(argv_info)
                    if not flag:
                        break
                elif argv_info[2] == 'int':
                    flag, cm, msg = self.check_int(argv_info)
                    if not flag:
                        break
                elif argv_info[2] == 'float':
                    flag, cm, msg = self.check_float(argv_info)
                    if not flag:
                        break
                elif argv_info[2] == 'list':
                    flag, cm, msg = self.check_list(argv_info)
                    if not flag:
                        break
                elif argv_info[2] == 'dict':
                    flag, cm, msg = self.check_dict(argv_info)
                    if not flag:
                        break
                elif argv_info[2] == 'image':
                    flag, cm, msg = self.check_image(argv_info)
                    if not flag:
                        break
                elif argv_info[2] == 'file':
                    flag, cm, msg = self.check_file(argv_info)
                    if not flag:
                        break
        return self.all_params_valid, cm, msg
    
    def get_argv(self, argv):
        return self.parser_args.get(argv)


class SpecialCheck(object):
    def __init__(self, argv, err_msg=''):
        self.argv = argv
        self.err_msg = err_msg
        self.flag = False

    def check_register_type(self):
        value_set = set()
        for key in RegisterEnum.__dict__.keys():
            if not key.startswith('_'):
                value_set.add(key)
        if self.argv not in value_set:
            return self.flag, CodeType.ARGV_STR_INVALID_ERROR, self.err_msg
        self.flag = True
        return self.flag, CodeType.SUCCESS_RESPONSE, ''

    def check_login_type(self):
        """
        同register
        :return:
        """
        return self.check_register_type()

    def check_login_method(self):
        value_set = set()
        for key in LoginMethodEnum.__dict__.keys():
            if not key.startswith('_'):
                value_set.add(key)
        if self.argv not in value_set:
            return self.flag, CodeType.ARGV_STR_INVALID_ERROR, self.err_msg
        self.flag = True
        return self.flag, CodeType.SUCCESS_RESPONSE, ''

    def check_gender_type(self):
        value_set = set()
        for key in GenderEnum.__dict__.keys():
            if not key.startswith('_'):
                value_set.add(key)
        if self.argv not in value_set:
            return self.flag, CodeType.ARGV_STR_INVALID_ERROR, self.err_msg
        self.flag = True
        return self.flag, CodeType.SUCCESS_RESPONSE, ''

    def check_permission_type(self):
        value_set = set()
        for key in PermissionEnum.__dict__.keys():
            if not key.startswith('_'):
                value_set.add(key)
        if self.argv not in value_set:
            return self.flag, CodeType.ARGV_STR_INVALID_ERROR, self.err_msg
        self.flag = True
        return self.flag, CodeType.SUCCESS_RESPONSE, ''
                
            

    

