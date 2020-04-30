'''
获取粉丝
'''
import json
from interceptors.interceptor import Interceptor
from model.db_helper import db
from mitmproxy import http
from utils.data_util import pack_user

class FansInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/user/follower/list/')

    def request(self, flow:http.HTTPFlow):
        pass

    def response(self,flow:http.HTTPFlow):
        print("FansInterceptor matched------------------------------")
        # print("-------------------------------\n" + str(flow.request.query) + "\n----------------------------")
        # print("------------uid:" + str(flow.request.query['user_id']))

        user_id = flow.request.query['user_id']

        for user in json.loads(flow.response.text)['followers']:
            if user['author']['short_id']:
                user_info = pack_user(user)
                db.save_user(user_info)

                fans = {}
                fans['uid'] = user_id
                fans['fid'] = user['uid']
                db.save_fans(fans)
            # print("-------------------------------\n" + str(fans) + "\n----------------------------")
