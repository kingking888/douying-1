import json

from interceptors.interceptor_fans import FansInterceptor
from interceptors.interceptor_comments import CommentsInterceptor
from interceptors.interceptor_userinfo import UserInfoInterceptor
from mitmproxy import http

interceptors = [CommentsInterceptor(),FansInterceptor(),UserInfoInterceptor()]



class Listener:

    def __init__(self):
        pass

    def request(self,flow:http.HTTPFlow):
        # print("-------------------------------request url:" + flow.request.pretty_url)
        for interceptor in interceptors:
            if interceptor.match(flow):
                interceptor.request(flow)

    def response(self,flow:http.HTTPFlow):
        # print("-------------------------------response url:" + flow.request.pretty_url)
        for interceptor in interceptors:
            if interceptor.match(flow):
                interceptor.response(flow)


addons=[
    Listener()
]
