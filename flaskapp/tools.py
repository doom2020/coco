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


if __name__ == "__main__":
    t1 = Test('aa')
    t2 = Test('bb')
    print(id(t1), id(t2))