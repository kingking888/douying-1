import json

from interceptors.interceptor_fans import FansInterceptor
from interceptors.interceptor_comments import CommentsInterceptor
from interceptors.interceptor_userinfo import UserInfoInterceptor
from interceptors.interceptor_videolist import VideoListInterceptor
from interceptors.interceptor_search import SearchInterceptor
from mitmproxy import http

interceptors = [CommentsInterceptor(),SearchInterceptor(),VideoListInterceptor(),FansInterceptor(),UserInfoInterceptor()]
dictInterceptors = dict()
def registerInterceptor(Interceptor):
    handler = Interceptor()
    dictInterceptors['path'] = Interceptor()

# registerInterceptor(CommentsInterceptor)
# registerInterceptor(VideoListInterceptor)
# registerInterceptor(FansInterceptor)
# registerInterceptor(UserInfoInterceptor)

class Listener:

    def __init__(self):
        pass

    def request(self,flow:http.HTTPFlow):
        # print("-------------------------------request url:" + flow.request.pretty_url)
        for interceptor in interceptors:
            if interceptor.match(flow):
                interceptor.request(flow)
                break

    def response(self,flow:http.HTTPFlow):
        for interceptor in interceptors:
            if interceptor.match(flow):
                interceptor.response(flow)
                break


addons=[
    Listener()
]
