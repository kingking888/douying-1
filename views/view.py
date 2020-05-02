# -*- coding: utf-8 -*-
# from mainui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from PyQt5.QtCore import *
import sys
import time
from utils.data_util import get_cur_keyword_id,set_cur_keyword_id
from model.db_helper import db
from views.uimainview import Ui_MainWindow

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent=parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)  # 隐藏关闭按钮

        self.btn_setkw_id.clicked.connect(self.set_keyword)
        self.btn_clear_kw.clicked.connect(self.clear_keyword)
        self.btn_refresh.clicked.connect(self.refresh)
        # self.btn_setkw_id.setToolTip("ddddddddddddddddd")



    def refresh(self):

        data = db.query_keyword(get_cur_keyword_id())
        if data == None:
            print(get_cur_keyword_id())
            self.lbl_cur_kw.setText("当前关键字ID:%s" % (str(get_cur_keyword_id())))
            self.lbl_tip.setText(' 还未生成关键字数据,请现在抖音中搜索!')
            self.lbl_tip.setStyleSheet("color:rgb(255,0,0,255)")
        else:
            self.lbl_cur_kw.setText("当前关键字:%s ID:%d" % (data['keyword'],get_cur_keyword_id()))
            self.lbl_tip.setText('')




    def update_ui(self,*args):
        self.refresh()

    def set_keyword(self):
        set_cur_keyword_id(int(self.lineEdit_search.text()))
        self.refresh()

    def clear_keyword(self):
        set_cur_keyword_id(-1)
        self.refresh()




if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MainView()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())