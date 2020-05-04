
from model.db_mongo import MongoDB

db = MongoDB()

class DYModel():
    def __init__(self):
        self.video_datas = []

    def is_too_much_videos(self):
        return len(self.video_datas) > 5

    def pop_video(self):
        if len(self.video_datas) > 0:
            return self.video_datas.pop(0)
        return None

    def add_video(self,video):
        self.video_datas.append(video)


dy_model = DYModel()