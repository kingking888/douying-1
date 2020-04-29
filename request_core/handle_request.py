from request_core.comment_queue import commentQueue
from handle_db import mongo_info
import requests
from urllib import parse


def generate_url(info):

    query = info['query']
    query_str = ''
    for k in query.keys():
        if query_str != '':
            query_str += "&"
        query_str += "%s=%s"%(k,query[k])

    query_str = parse.urlencode(query)
    url = "%s://%s%s?%s"%(info['scheme'],info['host'],info['path'],query_str)

    return url
rst_info = mongo_info.get_request_info('/aweme/v2/comment/list/')
print(generate_url(rst_info))
url = rst_info['url']

# url = "https://aweme-hl.snssdk.com/aweme/v1/aweme/detail/?version_code=6.5.0&pass-region=1&pass-route=1&js_sdk_version=1.16.2.7&app_name=aweme&vid=9D5F078E-A1A9-4F64-81C7-F89CA6A3B1DC&app_version=6.5.0&device_id=34712926793&channel=App%20Store&mcc_mnc=46011&aid=1128&screen_width=750&openudid=263bd93f02801d126ca004edccbff8f6e1b19f51&os_api=18&ac=WIFI&os_version=12.3.1&device_platform=iphone&build_number=65014&device_type=iPhone9,1&iid=74239983401&idfa=F39B285A-4B4F-4874-9D7E-C728A892BF6D"
# data = {"aweme_id": video_id}
headers = rst_info['headers']
ret = {}
del headers[':authority']
res = requests.get(url, headers=headers,verify=False)
# print("status_code:" + res.status_code)
print(res.content.decode('gbk'))