'''
获取粉丝
'''
import json
from interceptors.interceptor import Interceptor
from handle_db import mongo_info
from mitmproxy import http

class FansInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/user/follower/list/')

    def request(self, flow:http.HTTPFlow):
        pass

    def response(self,flow:http.HTTPFlow):
        print("FansInterceptor matched------------------------------")
        for user in json.loads(flow.response.text)['followers']:
            user_info = Interceptor.packUser(self,user)
            mongo_info.save_user(user_info)
