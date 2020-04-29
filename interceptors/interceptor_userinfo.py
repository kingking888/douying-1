'''
拦截用户信息接口
'''

import json
from interceptors.interceptor import Interceptor
from handle_db import mongo_info
from mitmproxy import http

class UserInfoInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/user/profile/other/')

    def request(self, flow:http.HTTPFlow):
        pass

    def response(self,flow:http.HTTPFlow):
        print("UserInfoInterceptor matched------------------------------")
        user        = json.loads(flow.response.text)['user']
        user_info   = Interceptor.packUser(self,user)
        # print("************************************************************************\n"+ str(user_info) + "\n************************************************************************")
        mongo_info.save_user(user_info)
