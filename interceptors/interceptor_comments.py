#评论拦截器
import json
from interceptors.interceptor import Interceptor
from handle_db import mongo_info
from mitmproxy import http

class CommentsInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self, '/aweme/v2/comment/list/')
        #self.aweme_id = ""

    def request(self, flow:http.HTTPFlow):
        #self.aweme_id = flow.request.query.get("aweme_id")
        pass

    def response(self,flow):
        print("CommentsInterceptor matched------------------------------")
        for comment in json.loads(flow.response.text)['comments']:
            user_info = Interceptor.packUser(self,comment['user'])
            mongo_info.save_user(user_info)

            cmt_info = {}

            cmt_info['cid']         = comment['cid']
            cmt_info['vid']    = comment['aweme_id']
            cmt_info['uid']         = comment['user']['uid']
            cmt_info['content']        = comment['text']
            cmt_info['createtime'] = comment['create_time'] #
            cmt_info['digg_count']  = comment['digg_count'] #评论点赞数量
            mongo_info.save_comment(cmt_info)