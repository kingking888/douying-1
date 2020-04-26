
class Interceptor:
    def __init__(self,path):
        self.path = path

    def intercepted(self,flow):
        url = flow.request.url
        return self.path in url

    def handle(self,flow):
        raise Exception("必须由子类覆盖Interceptor.handle方法!!!!!!!!")
