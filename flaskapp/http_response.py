import json


class HttpResponse:
    def __init__(self, code=200, success=True, result={}, message=''):
        self.code = code
        self.success = success
        self.result = result
        self.message = message

    def to_dict(self):
        return json.dumps(self.__dict__)
    
# if __name__ == "__main__":
#     hr = HttpResponse()
#     hr.to_dict()


# class CodeMessage(object):
#     def __init__(self, code=100, message=''):
#         self.code = code
#         self.message = message



class CodeType(object):
    """
    响应状态码规则
    参数校验(1000 ~ 1999)
    1000 通用参数错误(参数为空)
    1100 字符类型校验(1101~1199)
    1200 整数类型校验(1201~1299)
    1300 浮点类型校验(1301~1399)
    1400 列表类型校验(1401~1499)
    1500 字典类型校验(1501~1599)
    1600 图片类型校验(1601~1699)
    1700 文件类型校验(1701~1799)
    """

    class CodeMessage(object):
        def __init__(self, code, message):
            self.code = code
            self.message = message

    # 参数相关响应码
    ARGV_IS_BLANK = CodeMessage(code=1000, message='argv is blank')
    ARGV_STR_TYPE_ERROR = CodeMessage(code=1101, message='argv is not str type')
    ARGV_INT_TYPE_ERROR = CodeMessage(code=1201, message='argv is not int type')
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

    # 通用响应码
    



