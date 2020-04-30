#评论拦截器
import json
from interceptors.interceptor import Interceptor
from model.db_helper import db
from mitmproxy import http
from utils.data_util import pack_user,pack_comment,pack_comment_1

class CommentReplyInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self, '/aweme/v1/comment/list/reply/')
        #self.aweme_id = ""

    def request(self, flow:http.HTTPFlow):
       pass

    def response(self,flow):
        print("CommentsInterceptor matched------------------------------")
        for comment in json.loads(flow.response.text)['comments']:
            if comment['user']['short_id']:
                user_info = pack_user(comment['user'])
                db.save_user(user_info)

                cmts = pack_comment_1(comment)
                db.save_comments(cmts)