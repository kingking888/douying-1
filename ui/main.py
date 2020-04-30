from res.ui.mainui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.btn_search.clicked.connect(self.search)

    def search(self):
        print("search")


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Main()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())