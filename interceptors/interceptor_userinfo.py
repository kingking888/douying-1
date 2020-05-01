'''
拦截用户信息接口
'''

import json
from interceptors.interceptor import Interceptor
from model.db_helper import db
from mitmproxy import http
from utils.data_util import pack_user,get_cur_keyword_id

class UserInfoInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/user/profile/other/')


    def response(self,flow:http.HTTPFlow):
        print("UserInfoInterceptor matched------------------------------")
        keyword_id = self.get_cur_keyword_id()

        if keyword_id > 0:
            user        = json.loads(flow.response.text)['user']
            if user['short_id']:
                user_info   = pack_user(user)
                db.save_user(user_info,keyword_id)
