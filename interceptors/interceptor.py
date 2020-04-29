from mitmproxy import http
from handle_db import mongo_info
class Interceptor:
    def __init__(self,path):
        self.path = path

    def match(self, flow:http.HTTPFlow):
        url = flow.request.url
        return self.path in url

    def request(self, flow:http.HTTPFlow):
        # 由子类覆盖Interceptor.request 方法!!!!!!!!
        self.save_request_info(flow)

    def response(self,flow:http.HTTPFlow):
        # 由子类覆盖Interceptor.response 方法!!!!!!!!
        pass


    def save_request_info(self,flow:http.HTTPFlow):
        data = {'path':self.path,'method':flow.request.method,'scheme':flow.request.scheme,'host':flow.request.host,'headers':flow.request.headers,'url':flow.request.url,'query':flow.request.query}
        mongo_info.save_request_info(data)

    def packUser(self,user):
        user_info = {}

        uid         = user.get('uid') #用户ID
        short_id    = user.get('short_id') #抖音id
        unique_id   = user.get('unique_id')
        nickname    = user.get('nickname') #昵称

        # 这里需要进行非空判断,有些没有值会覆盖之前的
        if uid and uid != "0":
            user_info['uid'] = uid
        if short_id and short_id != '0':
            user_info['short_id'] = short_id
        if unique_id and unique_id != '0':
            user_info['unique_id'] = unique_id
        if nickname:#昵称
            user_info['nike'] = nickname
        # 0 male 1 female 2 unset
        if user.get('gender'):#性别
            user_info['gender'] = user['gender']
        if user.get('birthday'):#生日
            user_info['birthday'] = user['birthday']

        if user.get('status'):
            user_info['status'] = user['status']
        if user.get('region'):
            user_info['region'] = user['region']

        # 作品数量
        if user.get('aweme_count'):
            user_info['aweme_count'] = user['aweme_count']
        # 获赞数量
        if user.get('total_favorited'):
            user_info['total_favorited'] = user['total_favorited']
        # 关注数量
        if user.get('following_count'):
            user_info['following_count'] = user['following_count']
        # 粉丝数量
        if user.get('follower_count'):
            user_info['follower_count'] = user['follower_count']
        # 签名
        if user.get('signature'):
            user_info['signature'] = user.get('signature')
        #学校
        if user.get('school_name'):
            user_info['school_name'] = user.get('school_name')
        # 地区
        if user.get('area'):
            user_info['district'] = user.get('district')
        # 位置
        if user.get('location'):
            user_info['location'] = user.get('location')
        #省份
        if user.get('province'):
            user_info['province'] = user.get('province')

        #国家
        if user.get('country'):
            user_info['country'] = user.get('country')
        #城市
        if user.get('city'):#
            user_info['city'] = user.get('city')
        if user.get('twitter_name'):#
            user_info['twitter_name'] = user.get('twitter_name')
        #头像
        if user.get('avatar_medium') and len(user.get('avatar_medium').get("url_list")) > 0:
            user_info['head_icon'] = user.get('avatar_medium').get("url_list")[0]

        followers_detail = user.get('followers_detail')
        if followers_detail:
            for v in followers_detail:
                if v['app_name'] == 'aweme':
                    user_info['fans_count'] = user.get('fans_count')#粉丝数量
                    break

        return user_info
