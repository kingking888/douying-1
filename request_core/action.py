import requests
import urllib3
import json
from urllib import parse
from model.db_helper import db
from model.vo import RequestVO


class Action():
    def __init__(self,path):
        self.path = path
        self.requestVO = RequestVO(db.get_request_info(self.path))

    def get_url(info):

        query = info['query']
        query_str = ''
        for k in query.keys():
            if query_str != '':
                query_str += "&"
            query_str += "%s=%s" % (k, query[k])

        query_str = parse.urlencode(query)
        url = "%s://%s%s?%s" % (info['scheme'], info['host'], info['path'], query_str)
        return url


class SearchAction(Action):
    def __init__(self):
        super(SearchAction,self).__init__('/aweme/v1/general/search/single/')


    def search(self,word):
        session = requests.Session()
        requests.packages.urllib3.disable_warnings()
        headers = self.requestVO.headers
        del headers[':authority']

        info = self.requestVO.get_search_url(word)

        res = None

        if self.requestVO.isGet():
            res = session.get(info['url'], headers=headers, verify=False)
        else:
            res = session.post(info['url'],data=info['query'], headers=headers, verify=False)


        return res


import time
print(time.time())

search = SearchAction()
rst = search.search("减肥计划")
print(rst.content)