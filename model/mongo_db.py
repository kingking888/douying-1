import pymongo
import re
from lib.difflib import SequenceMatcher

class MongoDB(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="127.0.0.1",port=27017)
        self.db = self.client["douyindb"]


    # 评论
    def save_comment(self,data):
        tb = self.db["comment"]
        # aweme_id 视频ID
        tb.find_one_and_update({'cid':data['cid']},{'$set':data},upsert=True)

    def save_comments(self,datas):
        # tb = self.db["comment"]
        # tb.update_many({})
        # tb.insert_many()
        for v in datas:
            self.save_comment(v)


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
    def save_user(self,data,keyword_id):
        tb = self.db["user"]
        if data.get('short_id'):
            # db.col.update({"name": "kad"}, {$addToSet: {"tags": "mysql"}});
            # print("-----------------keyword_id:%s--------------"%keyword_id)
            tb.find_one_and_update({'short_id':data.get('short_id')},{'$set':data,"$addToSet":{'keywords':keyword_id}},upsert=True)
        # elif data.get('unique_id'):
        #     tb.find_one_and_update({'unique_id': data.get('unique_id')}, {'$set': data}, upsert=True)
        # elif data.get('uid'):
        #     tb.find_one_and_update({'uid': data.get('uid')}, {'$set': data}, upsert=True)
        else:
            print("warning::save_user update failed,cant get short_id or unique_id or uid!!!!!!")

    # 保存粉丝
    def save_fans(self,data):
        tb = self.db['fans']
        tb.find_one_and_update({'uid': data.get('uid'),'fid':data.get('fid')}, {'$set': data}, upsert=True)

    # 保存粉丝
    def save_video(self, data):
        tb = self.db['video']
        # vid 视频ID
        tb.find_one_and_update({'uid': data.get('uid'), 'vid': data.get('vid')}, {'$set': data}, upsert=True)

    global max_keyword_id
    max_keyword_id = -1
    # 查找关键字,按相似都查找,没有找到则插入
    def find_insert_keyword(self,data):
        tb = self.db['keywords']
        # 包含
        # item = tb.find_one({'keyword':re.compile(data['keyword'])})
        # 相似度
        (item,similar) = self.find_max_similar_keyword(data['keyword'])

        if similar < 0.6:
            item = None

        if item == None:
            global max_keyword_id
            if max_keyword_id == -1:
                cursor = tb.find().sort('keyword_id',-1)
                if cursor.collection.count_documents({}) == 0:
                    max_keyword_id = 0
                else:
                    max_keyword_id = cursor[0]['keyword_id']
            max_keyword_id += 1
            data['keyword_id'] = max_keyword_id
            data['_id'] = tb.insert_one(data).inserted_id
            item = data
        return item

    def find_max_similar_keyword(self,keyword):
        tb = self.db['keywords']
        items = tb.find()
        similar = 0
        item = None
        for v in items:
            kw = v['keyword']
            if keyword in kw or kw in keyword:
                item = v
                return item,1.0
            ratio = SequenceMatcher(lambda x: x == " ", kw, keyword).ratio()
            if ratio > similar:
                similar = ratio
                item = v
            # print("%s and %s similar ratio:%f" % (keyword,v['keyword'], ratio))
        return item,similar

    def handle_get_task(self):
        # 获取到数据，并删除数据库中的文档
        return self.db['douyin'].find_one_and_delete({})


