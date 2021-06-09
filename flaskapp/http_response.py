import json


class HttpResponse:
    def __init__(self, code=200, success=True, result={}, message=''):
        self.code = code
        self.success = success
        self.result = result
        self.message = message

    def to_dict(self):
        return json.dumps(self.__dict__)
    
if __name__ == "__main__":
    hr = HttpResponse()
    hr.to_dict()
