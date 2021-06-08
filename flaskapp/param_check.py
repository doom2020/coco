from flask import request, jsonify, Response

class ParamCheck(object):
    def __init__(self):
        self.args = []
        self.parser_args = {}

    def check_str(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1101, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, str):
                ret_dict = dict(code=1102, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, str):
                    ret_dict = dict(code=1103, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv


    def check_int(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1201, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, int):
                ret_dict = dict(code=1202, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, int):
                    ret_dict = dict(code=1203, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv

    def check_float(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1301, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, float):
                ret_dict = dict(code=1302, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, float):
                    ret_dict = dict(code=1303, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv

    def check_list(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1401, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, list):
                ret_dict = dict(code=1402, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, list):
                    ret_dict = dict(code=1403, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv

    def check_dict(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1501, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, dict):
                ret_dict = dict(code=1502, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, dict):
                    ret_dict = dict(code=1503, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv

    def check_image(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1601, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, str):
                ret_dict = dict(code=1602, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, str):
                    ret_dict = dict(code=1603, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv

    def check_file(self, argv_info):
        param, required, p_type, msg = argv_info
        argv = request.get_json(silent=True).get(param, '')
        if required:
            if not argv:
                ret_dict = dict(code=1701, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
            if not isinstance(argv, str):
                ret_dict = dict(code=1702, success=False, result={}, message=msg)
                return Response(jsonify(ret_dict))
        else:
            if argv:
                if not isinstance(argv, str):
                    ret_dict = dict(code=1703, success=False, result={}, message=msg)
                    return Response(jsonify(ret_dict))
        self.parser_args[param] = argv

    def params_add(self, param, required=False, p_type=None, msg=''):
        self.args.append((param, required, p_type, msg))

    def params_parser(self):
        if self.args:
            for _ in range(len(self.args)):
                argv_info = self.args.pop()
                if argv_info[2] == 'str':
                    self.check_str(argv_info)
                elif argv_info[2] == 'int':
                    self.check_int(argv_info)
                elif argv_info[2] == 'float':
                    self.check_float(argv_info)
                elif argv_info[2] == 'list':
                    self.check_list(argv_info)
                elif argv_info[2] == 'dict':
                    self.check_dict(argv_info)
                elif argv_info[2] == 'image':
                    self.check_image(argv_info)
                elif argv_info[2] == 'file':
                    self.check_file(argv_info)
    
    def get_argv(self, argv):
        return self.parser_args.get(argv)

    

