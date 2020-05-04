from mitmproxy import http
from model.model import db
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

    def save_request_info(self, flow: http.HTTPFlow):
        query = None
        request = flow.request
        if request.method.lower() == "get":
            query = request.query
        else:
            query = request.urlencoded_form

        token = request.cookies.get('uid_tt') or ''

        data = {'path': self.path, 'method': request.method, 'token': token,
                'scheme': request.scheme, 'host': request.host, 'headers': request.headers, 'url': request.url,
                'query': request.query, 'form': request.urlencoded_form}
        db.save_request_info(data)

