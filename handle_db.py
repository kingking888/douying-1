import pymongo

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="127.0.0.1",port=27017)
        self.db = self.client["douyindb"]


    # 评论
    def save_comment(self,data):
        tb = self.db["comment"]
        # aweme_id 视频ID
        tb.find_one_and_update({'cid':data['cid']},{'$set':data},upsert=True)

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
    def save_fans(self,data):
        tb = self.db['fans']
        tb.find_one_and_update({'uid': data.get('uid'),'fid':data.get('fid')}, {'$set': data}, upsert=True)


    def handle_get_task(self):
        # 获取到数据，并删除数据库中的文档
        return self.db['douyin'].find_one_and_delete({})

    # def packUser(self,user):
    #     user_info = {}
    #
    #     uid         = user.get('uid')
    #     short_id    = user.get('short_id')
    #     unique_id   = user.get('unique_id')
    #     nickname    = user.get('nickname')
    #
    #     if uid and uid != "0":
    #         user_info['uid'] = uid
    #     if short_id and short_id != '0':
    #         user_info['short_id'] = short_id
    #     if unique_id and unique_id != '0':
    #         user_info['unique_id'] = unique_id
    #     if nickname:
    #         user_info['nickname'] = nickname
    #     # 0 male 1 female 2 unset
    #     if user.get('gender'):
    #         user_info['gender'] = user['gender']
    #     if user.get('birthday'):
    #         user_info['birthday'] = user['birthday']
    #     if user.get('status'):
    #         user_info['status'] = user['status']
    #     if user.get('region'):
    #         user_info['region'] = user['region']
    #     # 这里需要进行非空判断,有些没有值会覆盖之前的
    #     if user.get('signature'):
    #         user_info['signature'] = user.get('signature')
    #     return user_info

mongo_info=Connect_mongo()
# mongo_info.save_user(mongo_info.packUser({'short_id':1,'nickname':'smw'}))
# mongo_info.save_user(mongo_info.packUser({'short_id':1,'unique_id':'10000'}))
# mongo_info.save_user(mongo_info.packUser({'short_id':1,'unique_id':'0'}))
# mongo_info.save_comment({'uid':1,"aweme_id":'1','text':'test text'})
# mongo_info.save_comment({'uid':1,"aweme_id":'1','text':'test text'})
