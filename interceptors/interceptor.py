from mitmproxy import http
from model.db_helper import db
from utils.data_util import get_cur_keyword_id

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

    def get_cur_keyword_id(self):
        keyword_id = get_cur_keyword_id()

        if keyword_id <= 0:
            print("warning::%s.response keyword_id is unset,please search first!!!!!!" % self.__class__.__name__)
            return -1
        return keyword_id



    def save_request_info(self,flow:http.HTTPFlow):
        query = None
        if flow.request.method.lower() == "get":
            query = flow.request.query
        else:
            query = flow.request.urlencoded_form

        data = {'path':self.path,'method':flow.request.method,'scheme':flow.request.scheme,'host':flow.request.host,'headers':flow.request.headers,'url':flow.request.url,'query':query}
        db.save_request_info(data)

