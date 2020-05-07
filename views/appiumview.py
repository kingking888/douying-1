from appium import webdriver

from model.model import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from views.res import *

import time
import random


class Action():
    def __init__(self,driver,owner=None):
        self.driver         = driver
        self.owner          = owner

        self._finished      = False

    def set_owner(self,owner):
        self.owner = owner

    def enter(self,*args,**kwargs):
        self._finished = False

    def execute(self,*args,**kwargs):
        pass

    def destroy(self):
        pass

    def is_finished(self):
        return self._finished

    def get_rnd(self,min,max):
        return random.random() * (max - min) + min

    def get_win_size():
        # 获取设备屏幕大小
        win_size = self.driver.get_window_size()
        x = win_size['width']
        y = win_size['height']
        return x, y

    def send_return_event(self):
        print("按回车需要安装第三方输入法,比如搜狗")
        # 一下两句实现回车搜索,需要安装第三方输入法,比如搜狗
        self.driver.keyevent(66)
        self.driver.press_keycode(66)

    def back(self):
        time.sleep(self.get_rnd(0.05,0.15))
        self.driver.keyevent(4) #

class DouYinAction(Action):
    def __init__(self,driver,wait_time=10):
        super(DouYinAction, self).__init__(driver)
        self.dicEle = dict()
        self.wait = WebDriverWait(self.driver, wait_time)

    def find_element_by_id(self, id_, message='',use_timeout=True,force_find=False):
        ele = self.dicEle.get(id_)
        if ele and ele.is_displayed() and force_find == False:
            return ele

        try:
            if use_timeout > 0:
                ele = self.wait.until(lambda x:x.find_element_by_id(id_),message=message)
            else:
                ele = self.driver.find_element_by_id(id_)
        except NoSuchElementException as e:
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
        except NoSuchElementException as e:
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
    # 返回到主界面
    def back2_home(self):
        while not self.isIndex():
            self.back()
            time.sleep(self.get_rnd(0.05,0.2))
    # 返回到搜索界面
    def back2_search_view(self):
        while not self.is_search_view():
            self.back()


    # 是否首页,注意没有做等待处理,只
    def isIndex(self,use_timeout=True):
        # ele = WebDriverWait(self.driver,0.3,ignored_exceptions=Exception).until(lambda driver:driver.find_element_by_id(INDEX_INDEX_TEXT))
        try:
            ele = self.find_element_by_id(INDEX_INDEX_TEXT,use_timeout=use_timeout,force_find=True)
            return ele != None
        except Exception:
            pass
        return False

    # 是否搜索页面
    def is_search_view(self):
        try:
            # ele = WebDriverWait(self.driver, 0.3, ignored_exceptions=Exception).until(
            #     lambda driver: driver.find_element_by_id(SEARCH_INPUT_TEXT))
            ele = self.find_element_by_id(SEARCH_INPUT_TEXT, use_timeout=False, force_find=True)
            return ele != None
        except Exception as e:
            pass
        return False


class SwipeAction(DouYinAction):
    def __init__(self,driver):
        super(SwipeAction, self).__init__(driver)

        self.swipe_count    = 1
        self.direction      = "up" # or 'down'
        self.delay_min      = 1
        self.delay_max      = 7

    def enter(self,*args,**kwargs):
        super(SwipeAction, self).enter(*args,**kwargs)

        win_size = self.driver.get_window_size()
        x = win_size['width']
        y = win_size['height']

        # self.size       = self.get_win_size()
        self.size = [x,y]
        self.direction  = kwargs.get("direction")   or "up"
        self.swipe_count= kwargs.get('swipe_count') or 1

        print("SwipeAction enter......")

    def execute(self,*args,**kwargs):
        print("SwipeAction execute......")
        if not self.is_finished():
            for i in range(0,self.swipe_count):

                x       = int(self.size[0] * self.get_rnd(0.3,0.6))
                s_y     = int(self.size[1] * self.get_rnd(0.05,0.3))
                b_y     = int(self.size[1] * self.get_rnd(0.7, 0.87))

                _from   = None
                _to     = None
                if self.direction == "up":
                    _from   = [x,b_y]
                    _to     = [x,s_y]
                elif self.direction == "down":
                    _to     = [x, b_y]
                    _from   = [x, s_y]

                print("start to swipe %d:from %f,%f to %f,%f" % (i, _from[0], _from[1], _to[0], _to[1]))
                self.driver.swipe(_from[0], _from[1], _to[0], _to[1])
                time.sleep(self.get_rnd(self.delay_min, self.delay_max))

            self._finished = True

class BatchSendPrtMsgAction(DouYinAction):
    '''
    批量发私信
    '''
    def __init__(self,driver):
        super(BatchSendPrtMsgAction, self).__init__(driver)

    def enter(self,*args,**kwargs):
        super(BatchSendPrtMsgAction, self).enter(*args,**kwargs)
        self.datas = kwargs.get("datas")
        print("BatchSendPrtMsgAction enter......")


    def execute(self,*args,**kwargs):
        super(BatchSendPrtMsgAction, self).execute(*args,**kwargs)
        print("BatchSendPrtMsgAction execute......")
        if not self.is_finished():
            if self.datas and len(self.datas) > 0:
                msg_action = SendPrtMsgAction(self.driver)
                for d in  self.datas:
                    msg_action.enter()
                    msg_action.execute(keyword=d.get('nike'))
                    msg_action.back2_search_view()
                    time.sleep(self.get_rnd(0.2,0.4))

                self._finished = True


    def open_search_view(self,keywrod):
        searchView = SendPrtMsgAction(self.driver)
        searchView.opt_prt_msg(keywrod)



class SendPrtMsgAction(DouYinAction):

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

    def enter(self,*args,**kwargs):
        super(SendPrtMsgAction, self).enter(*args,**kwargs)
        print("SendPrtMsgAction enter......")

    # 发送私信
    def execute(self,*args,**kwargs):
        print("SendPrtMsgAction execute......")

        keyword = kwargs.get("keyword")
        if keyword:
            if self.isIndex():
                self.open_search_view()
                time.sleep(self.get_rnd(0.06,0.2))
            self.input_search_text(keyword)
            time.sleep(self.get_rnd(0.06, 0.2))
            self.open_prt_view()
            time.sleep(self.get_rnd(0.06, 0.2))
            self.input_prt_msg()
            time.sleep(self.get_rnd(0.06, 0.2))
            self.send_prt_msg()
        self.is_finished = True

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
        arr = [{'unique_id':'','short_id':'62713337','nike':'来咯离婚率'}
            ,{'unique_id':'','short_id':'1100870146','nike':'嘘赵寅成睡着惹'}
            ,{'unique_id':'','short_id':'2301531913','nike':'朦胧的前途有你的存在'}]

        # adb connect 127.0.0.1:62001
        #driver = get_driver('127.0.0.1:62001', 62001)
        driver = get_driver('127.0.0.1:62001', 62025)
        # arr = driver.available_ime_engines
        # view = BatchSendPrtMsgAction(driver)
        view = SwipeAction(driver)

        time.sleep(2)

        view.enter(datas=arr,swipe_count=5)
        view.execute()
        time.sleep(10000)
        driver.close()
    except BaseException as e:
        print(e)
        driver.close()

    # driver.press_keycode(66)
    #  d = webdriver.Remote()
    # driver.find_element_by_xpath()
    # driver.find_element_by_class_name()

    # d.close()
    # d.keyevent()