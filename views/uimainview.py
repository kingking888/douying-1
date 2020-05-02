# -*- coding: utf-8 -*-

# Form implementation generated from reading views file 'main.views'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 601, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_cur_kw = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cur_kw.setGeometry(QtCore.QRect(11, 111, 581, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cur_kw.setFont(font)
        self.lbl_cur_kw.setObjectName("lbl_cur_kw")
        self.lbl_tip = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tip.setGeometry(QtCore.QRect(100, 140, 531, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.lbl_tip.setFont(font)
        self.lbl_tip.setText("")
        self.lbl_tip.setObjectName("lbl_tip")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.btn_refresh.setObjectName("btn_refresh")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 391, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_search = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_search.setToolTip("")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout.addWidget(self.lineEdit_search)
        self.btn_setkw_id = QtWidgets.QPushButton(self.widget)
        self.btn_setkw_id.setObjectName("btn_setkw_id")
        self.horizontalLayout.addWidget(self.btn_setkw_id)
        self.btn_clear_kw = QtWidgets.QPushButton(self.widget)
        self.btn_clear_kw.setStatusTip("")
        self.btn_clear_kw.setObjectName("btn_clear_kw")
        self.horizontalLayout.addWidget(self.btn_clear_kw)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "抖音"))
        self.label_3.setText(_translate("MainWindow", "注意,:如果关键字为-1,那么接下来第一次搜索产生的关键子会作为当前的关键字!"))
        self.lbl_cur_kw.setText(_translate("MainWindow", "当前关键字:-1"))
        self.btn_refresh.setText(_translate("MainWindow", "刷新"))
        self.label.setText(_translate("MainWindow", "请输入关键字ID:"))
        self.lineEdit_search.setText(_translate("MainWindow", "-1"))
        self.btn_setkw_id.setText(_translate("MainWindow", "设置"))
        self.btn_clear_kw.setText(_translate("MainWindow", "清除关键字"))
