'''
获取粉丝
'''
import json
from interceptors.interceptor import Interceptor
from mitmproxy import http
from google.protobuf.json_format import MessageToJson,Parse
from utils.data_util import pack_user
from model.db_helper import db


class VideoListInterceptor(Interceptor):
    def __init__(self):
        Interceptor.__init__(self,'/aweme/v2/feed/')

    def request(self, flow:http.HTTPFlow):
        pass

    def response(self,flow:http.HTTPFlow):
        print("VideoListInterceptor response------------------------------")
        print("*************************************")
        # print(flow.response.text)
        print("*************************************")
        # for user in json.loads(flow.response.text)['followers']:
        #     user_info = Interceptor.packUser(self,user)
        #     mongo_info.save_user(user_info)

    # # 将pbStringRequest【protobuf string类型的请求body】转化为json string以便解析请求中的某个指定参数
    # def pb_to_json(pbStringRequest){
    #     req = openrtb_pb2.BidRequest() 　　
    #     req.ParseFromString(pbStringRequest) 　　
    #     jsonStringRequest = MessageToJson(req)
    #     return jsonStringRequest
    # }
    #
    # # 将jsonStringResponse转化为pbString返回
    # def json_to_pb(jsonStringResponse){
    #     bidResponse = openrtb_pb2.BidResponse()
    #
    # Parse(jsonStringResponse, bidResponse)
    # pbStringResponse = bidResponse.SerializeToString()
    # return pbStringResponse
    # }