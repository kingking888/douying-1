import json

from interceptors.interceptor_fans import FansInterceptor
from interceptors.interceptor_comments import CommentsInterceptor
from interceptors.interceptor_userinfo import UserInfoInterceptor
from interceptors.interceptor_videolist import VideoListInterceptor
from interceptors.interceptor_search import SearchInterceptor
from interceptors.interceptor_comment_reply import CommentReplyInterceptor
from mitmproxy import http

# interceptors = [CommentsInterceptor(),SearchInterceptor(),VideoListInterceptor(),FansInterceptor(),UserInfoInterceptor()]
# interceptors = [SearchInterceptor()]

dictInterceptors = dict()
def registerInterceptor(Interceptor):
    handler = Interceptor()
    dictInterceptors[handler.get_path()] = Interceptor()

registerInterceptor(CommentsInterceptor)
registerInterceptor(VideoListInterceptor)
registerInterceptor(FansInterceptor)
registerInterceptor(UserInfoInterceptor)
registerInterceptor(SearchInterceptor)
registerInterceptor(CommentReplyInterceptor)

class Listener:

    def __init__(self):
        pass

    def request(self,flow:http.HTTPFlow):
        path = flow.request.path.split("?")[0]
        handler = dictInterceptors.get(path)
        if handler != None:
            handler.request(flow)

    def response(self,flow:http.HTTPFlow):
        path = flow.request.path.split("?")[0]
        handler = dictInterceptors.get(path)
        if handler != None:
            handler.response(flow)



addons=[
    Listener()
]
