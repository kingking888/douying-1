'''
获取粉丝
'''
import json
from interceptors.interceptor import Interceptor

class FansInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'aweme/v1/user/follower/list/')

    def handle(self,flow):
        print("*************************************************")
        for user in json.loads(flow.response.text)['followers']:
            user_info = {}
            user_info['share_id'] = user['uid']
            user_info['douyin_id'] = user['short_id']
            user_info['nickname'] = user['nickname']
            # 0 male 1 female 2 unset
            user_info['gender'] = user['gender']
            user_info['birthday'] = user['birthday']
            user_info['status'] = user['status']
            user_info['region'] = user['region']
            print(user_info)
