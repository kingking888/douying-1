import requests
import urllib3
import json
import time
import random

from urllib import parse
from model.db_helper import db
from model.vo import RequestVO
from model.model import dy_model
from model.vo import CommentListRequestVO,SearchRequestVO


class Action():
    def __init__(self,path,RequestVO=None):
        self.path       = path

        if RequestVO:
            self.requestVO  = RequestVO(db.get_request_info(self.path))

        self.session:requests.Session    = None

    def run(self):
        pass

    def do_request(self,*args, **kwargs):
        if self.session == None:
            self.session = requests.Session()
        requests.packages.urllib3.disable_warnings()

        headers = self.requestVO.headers
        del headers[':authority']

        info = self._get_url(*args,**kwargs)

        res = None

        if info:
            # info['url'] = 'https://api3-normal-c-lq.amemv.com/aweme/v2/comment/list/?aweme_id=6821531622433737987&cursor=0&count=20&address_book_access=1&gps_access=1&forward_page_type=1&channel_id=0&city=140900&hotsoon_filtered_count=0&hotsoon_has_more=0&page_source=0&os_api=22&device_type=OPPO%20R11&ssmix=a&manifest_version_code=100801&dpi=240&uuid=866174669451276&app_name=aweme&version_name=10.8.0&ts=1588292446&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=10809900&channel=tengxun_new&_rticket=1588292447405&device_platform=android&iid=1486171637029821&version_code=100800&cdid=36e6807f-6a17-42d0-b4c8-0e22124cfefc&openudid=dc53605f7f946658&device_id=800076378407783&resolution=720*1280&os_version=5.1.1&language=zh&device_brand=OPPO&aid=1128&mcc_mnc=46007'

            if self.requestVO.isGet():
                res = self.session.get(info['url'], headers=headers, verify=False)
            else:
                res = self.session.post(info['url'], data=info['query'], headers=headers, verify=False)
        else:
            print("warning::Action.do_request cant get request info!!!")

        return res

    def _get_url(self,*args, **kwargs):
        return self.requestVO.get_url(*args,**kwargs)
        # raise Exception("must be implemention by child!")

    def destroy(self):
        if self.session:
            self.session.close()
            self.session = None

class BrushComment(Action):
    def __init__(self):
        super(BrushComment, self).__init__('/aweme/v2/comment/list/',CommentListRequestVO)

    def run(self):
        while True:
            data = dy_model.pop_video()
            if data == None:
                print("cant get video data,waiting........")
            else:
                # self.requestVO.get_url(cursor=0,aweme_id=)
                time.sleep(random.uniform(0.5, 2))













class SearchAction(Action):
    # 协议无法使用
    def __init__(self):
        super(SearchAction,self).__init__('/aweme/v1/general/search/single/',SearchRequestVO)


    def search(self,word):
        return self.do_request(keyword=word)




import time
print(time.time())

bc = BrushComment()
# rst = bc.search("减肥计划")
rst = bc.do_request(aweme_id="6722776995547122957")
print(rst.content.decode())

# bc = SearchAction()
# res = bc.search("减肥")
# print(res.content.decode())