import json

from interceptors.interceptor_fans import FansInterceptor
from interceptors.interceptor_comments import CommentsInterceptor
from interceptors.interceptor_userinfo import UserInfoInterceptor
from interceptors.interceptor_videolist import VideoListInterceptor
from interceptors.interceptor_search import SearchInterceptor
from interceptors.interceptor_comment_reply import CommentReplyInterceptor
from mitmproxy import http
from optparse import OptionParser
from utils.data_util import set_cur_keyword_id

from res.ui.mainui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import _thread


# interceptors = [CommentsInterceptor(),SearchInterceptor(),VideoListInterceptor(),FansInterceptor(),UserInfoInterceptor()]
# interceptors = [SearchInterceptor()]

dictInterceptors = dict()
def registerInterceptor(Interceptor):
    handler = Interceptor()
    dictInterceptors[handler.get_path()] = Interceptor()

registerInterceptor(CommentsInterceptor)
registerInterceptor(VideoListInterceptor)
registerInterceptor(FansInterceptor)
registerInterceptor(UserInfoInterceptor)
registerInterceptor(SearchInterceptor)
registerInterceptor(CommentReplyInterceptor)

class Listener:

    def __init__(self):
        pass

    def request(self,flow:http.HTTPFlow):
        path = flow.request.path.split("?")[0]
        handler = dictInterceptors.get(path)
        if handler != None:
            handler.request(flow)

    def response(self,flow:http.HTTPFlow):
        path = flow.request.path.split("?")[0]
        handler = dictInterceptors.get(path)
        if handler != None:
            handler.response(flow)





def main():
    parser = OptionParser()
    parser.add_option('-kw','--keyword',default=-1,dest='keyword',help='set a keyword if you want to continue before.')
    (opts,args) = parser.parse_args()

    keyword = opts['keyword']
    set_cur_keyword_id(keyword)
    print("-------------------------kw:%s" % keyword)

    addons = [
        Listener()
    ]
# 只能放在最外面
# 如果没有设置keyword_id,则使用搜索产生的id(注意,只第一次设置)
addons = [
        Listener()
    ]

from ui.ui import MainView
def entry(threadname,delay):
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MainView()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())


_thread.start_new_thread(entry,('ui thread',0.5))
# entry()

