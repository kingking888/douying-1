'''
获取粉丝
'''
import json
from core.interceptors import Interceptor
from model.model import db
from mitmproxy import http
from utils.data_util import pack_user


class FansInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/user/follower/list/')

    def response(self,flow:http.HTTPFlow):
        print("FansInterceptor matched------------------------------")
        # print("-------------------------------\n" + str(flow.request.query) + "\n----------------------------")
        # print("------------uid:" + str(flow.request.query['user_id']))

        keyword_id = self.get_cur_keyword_id()

        if keyword_id > 0:
            user_id = flow.request.query['user_id']

            for user in json.loads(flow.response.text)['followers']:
                if user.get('short_id'):
                    user_info = pack_user(user)
                    print("*********************************************")
                    print(user_info)
                    print("*********************************************")
                    db.save_user(user_info,keyword_id)

                    fans = {}
                    fans['uid'] = user_id
                    fans['fid'] = user['uid']
                    db.save_fans(fans)
                # print("-------------------------------\n" + str(fans) + "\n----------------------------")
