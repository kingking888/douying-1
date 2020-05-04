#评论拦截器
import json
from core.interceptors import Interceptor
from model.model import db
from utils.data_util import pack_user, pack_comment_1


class CommentReplyInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self, '/aweme/v1/comment/list/reply/')
        #self.aweme_id = ""


    def response(self,flow):
        print("CommentsInterceptor matched------------------------------")

        keyword_id = self.get_cur_keyword_id()
        if keyword_id > 0:
            for comment in json.loads(flow.response.text)['comments']:
                if comment['user'].get('short_id'):
                    user_info = pack_user(comment['user'])
                    db.save_user(user_info,keyword_id)

                    cmts = pack_comment_1(comment)
                    db.save_comments(cmts)