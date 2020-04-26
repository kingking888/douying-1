import pymongo

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="localhost",port=27017)
        self.db = self.client["douyindb"]

    def save_task(self, task):
        '保存粉丝信息'
        db_collection = self.db['douyin']
        # 找到就更新，没找到就新增
        db_collection.update({'share_id': task['share_id']}, task, True)

    def handle_get_task(self):
        # 获取到数据，并删除数据库中的文档
        return self.db['douyin'].find_one_and_delete({})

mongo_info=Connect_mongo()