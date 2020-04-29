import pymongo
import re

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="127.0.0.1",port=27017)
        self.db = self.client["douyindb"]


    # 评论
    def save_comment(self,data):
        tb = self.db["comment"]
        # aweme_id 视频ID
        tb.find_one_and_update({'cid':data['cid']},{'$set':data},upsert=True)


    def save_request_info(self,data):
        if not data['path']:
            print("warnning::save_request_info's path param is nil!!!!")
            return
        tb = self.db['request']
        tb.find_one_and_replace({'path':data['path']},data,upsert=True)

    def get_request_info(self,path):
        tb = self.db['request']
        return tb.find_one({'path':path})

    #保存用户
    def save_user(self,data):
        tb = self.db["user"]
        if data.get('short_id'):
            tb.find_one_and_update({'short_id':data.get('short_id')},{'$set':data},upsert=True)
        elif data.get('unique_id'):
            tb.find_one_and_update({'unique_id': data.get('unique_id')}, {'$set': data}, upsert=True)
        elif data.get('uid'):
            tb.find_one_and_update({'uid': data.get('uid')}, {'$set': data}, upsert=True)
        else:
            print("warning::save_user update failed,cant get short_id or unique_id or uid!!!!!!")

    # 保存粉丝
    def save_fans(self,data):
        tb = self.db['fans']
        tb.find_one_and_update({'uid': data.get('uid'),'fid':data.get('fid')}, {'$set': data}, upsert=True)

    global max_group_id
    max_group_id = -1
    def find_insert_keyword(self,data):
        tb = self.db['keywords']
        item = tb.find_one({'keyword':re.compile(data['keyword'])})
        tb.aggregate()

        if item == None:
            global max_group_id
            if max_group_id == -1:
                datas = tb.find({})
                print(datas.count())
                if datas.count() == 0:
                    max_group_id = 0
                else:
                    tmp = datas.collection.sort({"group_id":-1}).limit(1)
                    max_group_id = max_group_id
            max_group_id += 1
            data['group_id'] = max_group_id
            item = tb.insert_one(data)
        return item

    def handle_get_task(self):
        # 获取到数据，并删除数据库中的文档
        return self.db['douyin'].find_one_and_delete({})
mongo_info=Connect_mongo()
# mongo_info.save_user(mongo_info.packUser({'short_id':1,'nickname':'smw'}))
# mongo_info.save_user(mongo_info.packUser({'short_id':1,'unique_id':'10000'}))
# mongo_info.save_user(mongo_info.packUser({'short_id':1,'unique_id':'0'}))
# mongo_info.save_comment({'uid':1,"aweme_id":'1','text':'test text'})
# mongo_info.save_comment({'uid':1,"aweme_id":'1','text':'test text'})
#
mongo_info.find_insert_keyword({'keyword':"减肥"})
mongo_info.find_insert_keyword({'keyword':"嘟嘟减肥"})
