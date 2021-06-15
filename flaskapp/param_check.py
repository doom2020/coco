from flask import request
from flaskapp.http_response import CodeType
import ast
import traceback


class ParamCheck(object):
    def __init__(self):
        self.args = []
        self.parser_args = {}
        self.all_params_valid = True

    def check_str(self, argv_info):
        """
        字符串类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, str):
                self.all_params_valid = False
                return CodeType.ARGV_STR_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    return CodeType.ARGV_STR_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def check_int(self, argv_info):
        """
        整数类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, int):
                self.all_params_valid = False
                return CodeType.ARGV_INT_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, int):
                    self.all_params_valid = False
                    return CodeType.ARGV_INT_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def check_float(self, argv_info):
        """
        浮点类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, float):
                self.all_params_valid = False
                return CodeType.ARGV_FLOAT_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, float):
                    self.all_params_valid = False
                    return CodeType.ARGV_FLOAT_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def check_list(self, argv_info):
        """
        列表类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            try:
                argv = ast.literal_eval(argv)
            except Exception as e:
                print(traceback.format_exc(limit=1))
                self.all_params_valid = False
                return CodeType.ARGV_LIST_INVALID_ERROR, err_msg
            if not isinstance(argv, list):
                self.all_params_valid = False
                return CodeType.ARGV_LIST_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, list):
                    self.all_params_valid = False
                    return CodeType.ARGV_LIST_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def check_dict(self, argv_info):
        """
        字典类型校验
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            try:
                argv = ast.literal_eval(argv)
            except Exception as e:
                print(traceback.format_exc(limit=1))
                self.all_params_valid = False
                return CodeType.ARGV_DICT_INVALID_ERROR, err_msg
            if not isinstance(argv, dict):
                self.all_params_valid = False
                return CodeType.ARGV_DICT_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, dict):
                    self.all_params_valid = False
                    return CodeType.ARGV_DICT_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def check_image(self, argv_info):
        """
        图片校验(待完成)
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, str):
                self.all_params_valid = False
                return CodeType.ARGV_IMAGE_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    return CodeType.ARGV_IMAGE_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def check_file(self, argv_info):
        """
        文件校验(待完成)
        """
        param, required, p_type, err_msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                return CodeType.ARGV_IS_BLANK, err_msg
            if not isinstance(argv, str):
                self.all_params_valid = False
                return CodeType.ARGV_FILE_TYPE_ERROR, err_msg
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    return CodeType.ARGV_FILE_TYPE_ERROR, err_msg
        self.parser_args[param] = argv

    def params_add(self, param, required=False, p_type=None, err_msg=''):
        self.args.append((param, required, p_type, err_msg))

    def params_parser(self):
        cm, msg = None, None
        if self.args:
            for _ in range(len(self.args)):
                argv_info = self.args.pop()
                if argv_info[2] == 'str':
                    cm, msg = self.check_str(argv_info)
                    if cm:
                        break
                elif argv_info[2] == 'int':
                    cm, msg = self.check_int(argv_info)
                    if cm:
                        break
                elif argv_info[2] == 'float':
                    cm, msg = self.check_float(argv_info)
                    if cm:
                        break
                elif argv_info[2] == 'list':
                    cm, msg = self.check_list(argv_info)
                    if cm:
                        break
                elif argv_info[2] == 'dict':
                    cm, msg = self.check_dict(argv_info)
                    if cm:
                        break
                elif argv_info[2] == 'image':
                    cm, msg = self.check_image(argv_info)
                    if cm:
                        break
                elif argv_info[2] == 'file':
                    cm, msg = self.check_file(argv_info)
                    if cm:
                        break
        return self.all_params_valid, cm, msg
    
    def get_argv(self, argv):
        return self.parser_args.get(argv)

    

