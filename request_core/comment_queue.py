# 视频评论队列

class CommentQueue:
    def __init__(self):
        self.dic_ids = dict()
        self.queue = []

    def append(self,aweme_id):
        if self.dic_ids.get(aweme_id) == None:
            self.queue.append(aweme_id)
            self.dic_ids[aweme_id] = aweme_id
        else:
            print("CommentQueue::append %s has appended in queue,so is appended failed!"%aweme_id)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

commentQueue = CommentQueue()
