
class Interceptor:
    def __init__(self,path):
        self.path = path

    def match(self, flow):
        url = flow.request.url
        return self.path in url

    def request(self, flow):
        # 由子类覆盖Interceptor.request 方法!!!!!!!!
        pass

    def response(self,flow):
        # 由子类覆盖Interceptor.response 方法!!!!!!!!
        pass

    def packUser(self,user):
        user_info = {}

        uid         = user.get('uid')
        short_id    = user.get('short_id')
        unique_id   = user.get('unique_id')
        nickname    = user.get('nickname')

        if uid and uid != "0":
            user_info['uid'] = uid
        if short_id and short_id != '0':
            user_info['short_id'] = short_id
        if unique_id and unique_id != '0':
            user_info['unique_id'] = unique_id
        if nickname:
            user_info['nickname'] = nickname
        # 0 male 1 female 2 unset
        if user.get('gender'):
            user_info['gender'] = user['gender']
        if user.get('birthday'):
            user_info['birthday'] = user['birthday']
        if user.get('status'):
            user_info['status'] = user['status']
        if user.get('region'):
            user_info['region'] = user['region']
        # 这里需要进行非空判断,有些没有值会覆盖之前的
        if user.get('signature'): # 签名
            user_info['signature'] = user.get('signature')
        if user.get('school_name'):
            user_info['school_name'] = user.get('school_name')
        if user.get('district'):#地区
            user_info['district'] = user.get('district')
        if user.get('location'):  # 位置
            user_info['location'] = user.get('location')
        if user.get('country'):#
            user_info['country'] = user.get('country')
        if user.get('city'):#
            user_info['city'] = user.get('city')
        if user.get('twitter_name'):#
            user_info['twitter_name'] = user.get('twitter_name')
        return user_info
