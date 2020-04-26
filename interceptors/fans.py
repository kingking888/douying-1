'''
获取粉丝
'''
import json
from interceptors.interceptor import Interceptor
from handle_db import mongo_info

class FansInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'aweme/v1/user/follower/list/')

    def handle(self,flow):
        for user in json.loads(flow.response.text)['followers']:
            short_id = user['short_id']
            user_info = {}
            user_info['share_id'] = user['uid']
            user_info['douyin_id'] = short_id
            user_info['unique_id'] = user['unique_id']
            # if not short_id or short_id == '0' :
            #     user_info['douyin_id'] = user['unique_id']

            user_info['nickname'] = user['nickname']
            # 0 male 1 female 2 unset
            user_info['gender'] = user['gender']
            user_info['birthday'] = user['birthday']
            user_info['status'] = user['status']
            user_info['region'] = user['region']
            mongo_info.save_task(user_info)
