#评论拦截器
import json
from interceptors.interceptor import Interceptor
from model.db_helper import db
from mitmproxy import http
from utils.data_util import pack_user,pack_comment,pack_comment_1,get_cur_keyword_id

class CommentsInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self, '/aweme/v2/comment/list/')
        #self.aweme_id = ""


    def response(self,flow):
        print("CommentsInterceptor matched------------------------------")

        keyword_id = self.get_cur_keyword_id()

        if keyword_id > 0:
            for comment in json.loads(flow.response.text)['comments']:
                if comment['user']['short_id']:
                    user_info = pack_user(comment['user'])
                    db.save_user(user_info,keyword_id)

                    # cmt_info = pack_comment(comment)
                    # db.save_comment(cmt_info)

                    cmts = pack_comment_1(comment)
                    db.save_comments(cmts)