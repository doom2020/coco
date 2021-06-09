from flask import request
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
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1101, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, str):
                self.all_params_valid = False
                ret_dict = dict(code=1102, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    ret_dict = dict(code=1103, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def check_int(self, argv_info):
        """
        整数类型校验
        """
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1201, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, int):
                self.all_params_valid = False
                ret_dict = dict(code=1202, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, int):
                    self.all_params_valid = False
                    ret_dict = dict(code=1203, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def check_float(self, argv_info):
        """
        浮点类型校验
        """
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1301, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, float):
                self.all_params_valid = False
                ret_dict = dict(code=1302, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, float):
                    self.all_params_valid = False
                    ret_dict = dict(code=1303, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def check_list(self, argv_info):
        """
        列表类型校验
        """
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1401, success=False, result={}, message=msg)
                return ret_dict
            try:
                argv = ast.literal_eval(argv)
            except Exception as e:
                print(traceback.format_exc(limit=1))
                self.all_params_valid = False
                ret_dict = dict(code=1403, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, list):
                self.all_params_valid = False
                ret_dict = dict(code=1402, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, list):
                    self.all_params_valid = False
                    ret_dict = dict(code=1403, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def check_dict(self, argv_info):
        """
        字典类型校验
        """
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1501, success=False, result={}, message=msg)
                return ret_dict
            try:
                argv = ast.literal_eval(argv)
            except Exception as e:
                print(traceback.format_exc(limit=1))
                self.all_params_valid = False
                ret_dict = dict(code=1503, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, dict):
                self.all_params_valid = False
                ret_dict = dict(code=1502, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, dict):
                    self.all_params_valid = False
                    ret_dict = dict(code=1503, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def check_image(self, argv_info):
        """
        图片校验(待完成)
        """
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1601, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, str):
                self.all_params_valid = False
                ret_dict = dict(code=1602, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    ret_dict = dict(code=1603, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def check_file(self, argv_info):
        """
        文件校验(待完成)
        """
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                self.all_params_valid = False
                ret_dict = dict(code=1701, success=False, result={}, message=msg)
                return ret_dict
            if not isinstance(argv, str):
                self.all_params_valid = False
                ret_dict = dict(code=1702, success=False, result={}, message=msg)
                return ret_dict
        else:
            if argv:
                if not isinstance(argv, str):
                    self.all_params_valid = False
                    ret_dict = dict(code=1703, success=False, result={}, message=msg)
                    return ret_dict
        self.parser_args[param] = argv

    def params_add(self, param, required=False, p_type=None, msg=''):
        self.args.append((param, required, p_type, msg))

    def params_parser(self):
        ret_dict = {}
        if self.args:
            for _ in range(len(self.args)):
                argv_info = self.args.pop()
                if argv_info[2] == 'str':
                    ret_dict = self.check_str(argv_info)
                    if ret_dict:
                        break
                elif argv_info[2] == 'int':
                    ret_dict = self.check_int(argv_info)
                    if ret_dict:
                        break
                elif argv_info[2] == 'float':
                    ret_dict = self.check_float(argv_info)
                    if ret_dict:
                        break
                elif argv_info[2] == 'list':
                    ret_dict = self.check_list(argv_info)
                    if ret_dict:
                        break
                elif argv_info[2] == 'dict':
                    ret_dict = self.check_dict(argv_info)
                    if ret_dict:
                        break
                elif argv_info[2] == 'image':
                    ret_dict = self.check_image(argv_info)
                    if ret_dict:
                        break
                elif argv_info[2] == 'file':
                    ret_dict = self.check_file(argv_info)
                    if ret_dict:
                        break
        else:
            self.all_params_valid = False
            ret_dict = dict(code=1000, success=False, result={}, message='not any args')
        return self.all_params_valid, ret_dict
    
    def get_argv(self, argv):
        return self.parser_args.get(argv)

    

