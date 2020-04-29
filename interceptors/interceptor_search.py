'''
拦截搜索接口
'''

import json
from handle_db import mongo_info

from interceptors.interceptor import Interceptor
from handle_db import mongo_info
from mitmproxy import http
from urllib import parse



class SearchInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/general/search/single/')

    def request(self, flow:http.HTTPFlow):
        pass


    def response(self,flow:http.HTTPFlow):
        print("UserInfoInterceptor matched------------------------------")

        form_data = flow.request.urlencoded_form
        keyword = {'keyword':form_data['keyword']}

        key_info = mongo_info.find_insert_keyword(keyword)

        data        = json.loads(flow.response.text)['data']

        for v in data:
            if v['type'] == 1:
                aweme_info = v['aweme_info']
                user_info = Interceptor.packUser(self, aweme_info['author'])
                mongo_info.save_user(user_info)

