'''
拦截搜索接口
'''

import json
from core.interceptors import Interceptor
from model.model import db
from mitmproxy import http
from utils.data_util import pack_user,pack_video,get_cur_keyword_id,set_cur_keyword_id


class SearchInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v1/general/search/single/')


    def response(self,flow:http.HTTPFlow):
        print("SearchInterceptor matched------------------------------")

        form_data = flow.request.urlencoded_form
        keyword = {'keyword':form_data['keyword']}

        key_info = db.find_insert_keyword(keyword)
        keyword_id = key_info['keyword_id']

        if get_cur_keyword_id() == -1:
            set_cur_keyword_id(keyword_id)

        data  = json.loads(flow.response.text)['data']

        for v in data:
            if v['type'] == 1:
                aweme_info = v['aweme_info']
                # print("----------------------nickname:%s,short_id:%s" %(aweme_info['author']['nickname'],aweme_info['author']['short_id']))
                if aweme_info['author'].get('short_id'):
                    #-----------handle user-----------------
                    user_info = pack_user(aweme_info['author'])
                    # user_info['keyword_id'] = keyword_id
                    db.save_user(user_info,keyword_id)

                    #----------handle video-----------------
                    video   = pack_video(aweme_info)
                    video['uid'] = user_info['uid']
                    db.save_video(video)

