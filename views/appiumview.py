from appium import webdriver

from model.model import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from views.res import *

import time



class Action():
    def __init__(self,driver,owner=None,wait_time=15):
        self.driver = driver
        self.owner  = owner
        self.dicEle = dict()

        self.wait   = WebDriverWait(self.driver,wait_time)

    def set_owner(self,owner):
        self.owner = owner

    def find_element_by_id(self, id_, message='',use_timeout=True,force_find=False):
        ele = self.dicEle.get(id_)
        if ele and ele.is_displayed() and force_find == False:
            return ele

        try:
            if use_timeout > 0:
                ele = self.wait.until(lambda x:x.find_element_by_id(id_),message=message)
            else:
                ele = self.driver.find_element_by_id(id_)
        except Exception as e:
            ele = None
            print(e)

        self.dicEle[id_] = ele
        return  ele

    def find_elements_by_id(self, id_):
        return self.driver.find_elements_by_id(id_)

    def find_element_by_xpath(self,id_, message='',use_timeout=True,force_find=False):
        ele = self.dicEle.get(id_)
        if ele and ele.is_displayed() and force_find == False:
            return ele

        try:
            if use_timeout > 0:
                ele = self.wait.until(lambda x: x.find_element_by_xpath(id_), message)
            else:
                ele = self.driver.find_element_by_xpath(id_)
        except Exception as e:
            ele = None
            print(e)

        self.dicEle[id_] = ele
        return ele

    def find_element_by_xpath(self,path):
        self.driver.find_element_by_xpath(path)

    def click(self,id_,findType="id",message=''):
        ele = None
        if findType == "id":
            ele = self.wait.until(EC.element_to_be_clickable((By.ID,id_)),message=message)
            if ele:
                ele.click()
            else:
                print("cant get a element to click by id:%s" % id_)

            self.dicEle[id_] = ele
        else:
            raise Exception("View::click not implementation with %s" % findType)

        return ele

    def send_return_event(self):
        print("按回车需要安装第三方输入法,比如搜狗")
        # 一下两句实现回车搜索,需要安装第三方输入法,比如搜狗
        self.driver.keyevent(66)
        self.driver.press_keycode(66)

    # 是否首页,注意没有做等待处理,只
    def isIndex(self):
        ele = WebDriverWait(self.driver,0.3,ignored_exceptions=True).until(lambda driver:driver.find_element_by_id(INDEX_INDEX_TEXT))
        return ele != None





class BatchSendPrtMsgAction(Action):
    '''
    批量发私信
    '''
    def __init__(self,driver):
        super(BatchSendPrtMsgAction, self).__init__(driver)

    def open_search_view(self,keywrod):
        searchView = SendPrtMsgAction(self.driver)
        searchView.opt_prt_msg(keywrod)

class SendPrtMsgAction(Action):

    '''
    发私信
    '''
    def __init__(self,driver):
        super(SendPrtMsgAction, self).__init__(driver, self)

    # sh("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
    def sh(self, command):
        # https://blog.csdn.net/qq_42470033/article/details/89456878
        import subprocess
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


    # 发送私信
    def execute(self,keyword):
        self.open_search_view()
        self.input_search_text(keyword)
        self.open_prt_view()
        self.input_prt_msg()
        self.send_prt_msg()



    # 从搜界面打开搜索界面
    def open_search_view(self):
        print("open_search_view-->开始点击首页右上方的搜索按钮.")
        self.click(INDEX_SEARCH_BUTTON_ID, message="获取首页右上方搜索按钮报错.")

    # 输入搜索关键字
    def input_search_text(self,keyword):
        print("开始查找搜索界面上的输入框.")
        ele = self.click(SEARCH_INPUT_TEXT, message="获取首页右上方搜索按钮报错.")
        print("输入搜索关键字:%s" % keyword)
        # 输入关键字
        ele.send_keys(keyword)
        # 按回车
        self.send_return_event()

    # 打开私信界面
    def open_prt_view(self):
        print("open_prt_view-->查找用户信息上的粉丝文本并点击.")
        self.click(USERINFO_FANS_TEXT, message="查找用户信息上的粉丝文本并点击报错.")
        print("open_prt_view-->查找用户信息界面右上角三个小圆点按钮.")
        self.click(USERINFO_3_DOT, message="查找用户信息界面右上角三个小圆点按钮报错.")

    # 输入私信
    def input_prt_msg(self,msg=None):
        print("input_prt_msg-->查找发私信按钮.")
        self.click(USERINFO_PRTMSG_BTN, message="查找发私信按钮报错.")
        print("input_prt_msg-->查找发送消息输入框.")
        ele = self.click(PRTMSG_INPUT_TEXT, message="查找发送消息输入框报错.")
        ele.send_keys(msg or "拍的真好,我关注你啦,希望回关哦.")

    # 点击私信按钮
    def send_prt_msg(self):
        print("send_prt_msg-->查找发送按钮.")
        self.click(PRTMSG_SEND_BTN, message="查找发送按钮报错.")

'''
 运行环境:
 1.安装搜狗输入法(回车搜索需要)
 2.抖音 v10.9.0
 3.Appium
 4.夜神模拟器 v6.6.0.5202
'''
if __name__ == '__main__':
    driver = None
    try:
        # adb connect 127.0.0.1:62001
        #driver = get_driver('127.0.0.1:62001', 62001)
        driver = get_driver('127.0.0.1:62001', 62025)
        # arr = driver.available_ime_engines
        view = SendPrtMsgAction(driver)
        view.execute("海口浓情美容连锁")
        time.sleep(10000)
        driver.close()
    except Exception as e:
        print(e)
        driver.close()

    # driver.press_keycode(66)
    #  d = webdriver.Remote()
    # driver.find_element_by_xpath()
    # driver.find_element_by_class_name()

    # d.close()
    # d.keyevent()