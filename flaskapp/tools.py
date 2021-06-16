"""
通用工具模块
"""
import threading

class SingleInstance(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if SingleInstance._instance is None:
            SingleInstance._instance = super().__new__(cls)
        return SingleInstance._instance


class Test(SingleInstance):
    def __init__(self, name):
        self.name = name


# if __name__ == "__main__":
#     t1 = Test('aa')
#     t2 = Test('bb')
#     print(id(t1), id(t2))

class Pagination(object):
    def __init__(self, query_set, page_num=1, limit=15):
        self.query_set = query_set
        self.page_num = page_num
        self.limit = limit

    def page_result(self):
        data_set = self.query_set[(self.page_num - 1) * self.limit: (self.page_num *self.limit)]
        return data_set




    