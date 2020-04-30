from mitmproxy import http
from model.db_helper import db
class Interceptor:
    def __init__(self,path):
        self.path = path

    def get_path(self):
        return self.path

    def match(self, flow:http.HTTPFlow):
        url = flow.request.url
        return self.path in url

    def request(self, flow:http.HTTPFlow):
        # 由子类覆盖Interceptor.request 方法!!!!!!!!
        self.save_request_info(flow)

    def response(self,flow:http.HTTPFlow):
        # 由子类覆盖Interceptor.response 方法!!!!!!!!
        pass


    def save_request_info(self,flow:http.HTTPFlow):
        data = {'path':self.path,'method':flow.request.method,'scheme':flow.request.scheme,'host':flow.request.host,'headers':flow.request.headers,'url':flow.request.url,'query':flow.request.query}
        db.save_request_info(data)

