'''
拦截用户信息接口
'''

import json
from interceptors.interceptor import Interceptor
from model.db_helper import db
from mitmproxy import http
from utils.data_util import pack_user

class UserInfoInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/user/profile/other/')

    def request(self, flow:http.HTTPFlow):
        pass

    def response(self,flow:http.HTTPFlow):
        print("UserInfoInterceptor matched------------------------------")
        user        = json.loads(flow.response.text)['user']
        if user['author']['short_id']:
            user_info   = pack_user(user)
            db.save_user(user_info)
