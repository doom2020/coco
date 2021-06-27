import json


class CreateResponse(object):
    def __init__(self, cm, result={}, message=''):
        self.cm = cm
        self.result = result
        self.message = message

    def response(self):
        if self.cm == CodeType.SUCCESS_RESPONSE:
            success = True
        else:
            success = False
        if self.message:
            hr = HttpResponse(code=self.cm.code, success=success, result=self.result, message=self.message)
        else:
            hr = HttpResponse(code=self.cm.code, success=success, result=self.result, message=self.cm.message)
        return hr.to_dict()
            

class HttpResponse:
    def __init__(self, code=200, success=True, result={}, message=''):
        self.code = code
        self.success = success
        self.result = result
        self.message = message

    def to_dict(self):
        return json.dumps(self.__dict__)


class CodeType(object):
    """
    响应状态码规则
    -------------------------
    参数校验(1000 ~ 1999)
    1000 通用参数错误(参数为空)
    1100 字符类型校验(1101~1199)
    1200 整数类型校验(1201~1299)
    1300 浮点类型校验(1301~1399)
    1400 列表类型校验(1401~1499)
    1500 字典类型校验(1501~1599)
    1600 图片类型校验(1601~1699)
    1700 文件类型校验(1701~1799)
    --------------------------
    数据库相关(2000 ~ 2999)
    --------------------------
    工具类相关(3000 ~ 3999)
    """

    class CodeMessage(object):
        def __init__(self, code, message):
            self.code = code
            self.message = message

    # 成功响应码
    SUCCESS_RESPONSE = CodeMessage(code=200, message='')
    # 参数相关响应码
    ARGV_IS_BLANK = CodeMessage(code=1000, message='argv is blank')
    ARGV_STR_TYPE_ERROR = CodeMessage(code=1101, message='argv is not str type')
    ARGV_STR_INVALID_ERROR = CodeMessage(code=1102, message='argv is invalid')
    ARGV_INT_TYPE_ERROR = CodeMessage(code=1201, message='argv is not int type')
    ARGV_INT_INVALID_ERROR = CodeMessage(code=1202, message='argv is invalid')
    ARGV_FLOAT_TYPE_ERROR = CodeMessage(code=1301, message='argv is not float type')
    ARGV_LIST_TYPE_ERROR = CodeMessage(code=1401, message='argv is not list type')
    ARGV_LIST_INVALID_ERROR = CodeMessage(code=1402, message='argv is invalid')
    ARGV_DICT_TYPE_ERROR = CodeMessage(code=1501, message='argv is not dict type')
    ARGV_DICT_INVALID_ERROR = CodeMessage(code=1502, message='argv is invalid')
    ARGV_IMAGE_TYPE_ERROR = CodeMessage(code=1601, message='argv is not image type')
    ARGV_IMAGE_INVALID_ERROR = CodeMessage(code=1602, message='argv is invalid image')
    ARGV_FILE_TYPE_ERROR = CodeMessage(code=1701, message='argv is not file type')
    ARGV_FILE_INVALID_ERROR = CodeMessage(code=1702, message='argv is invalid file')

    # 数据库相关响应码
    DATABASE_ADD_ERROR = CodeMessage(code=2101, message='database add failed')
    DATABASE_QUERY_BLANK = CodeMessage(code=2201, message='database query is blank')
    DATABASE_QUERY_MANY = CodeMessage(code=2202, message='database query result not only one')
    DATABASE_QUERY_EXIST = CodeMessage(code=2203, message='database query result is exist')

    # 工具类相关响应码
    TOOL_ENCRYPT_STR_BLANK = CodeMessage(code=3101, message='encrypt str is blank')
    TOOL_ENCRYPT_STR_TYPE_ERROR = CodeMessage(code=3102, message='encrypt argv type is not str')

    # 通用响应码
    IMAGE_FILE_IS_NOT_EXIST = CodeMessage(code=9101, message='image file is not exist')
    ARGV_IS_NOT_FILE = CodeMessage(code=9102, message='argv is not file')
    IMAGE_SAVE_FAILED = CodeMessage(code=9103, message='image save is failed')

