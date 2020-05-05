from appium import webdriver

from model.model import get_driver
from selenium.webdriver.support.ui import WebDriverWait

import time



class View():
    def __init__(self,driver,owner=None,wait_time=15):
        self.driver = driver
        self.owner = owner

        self.wait   = WebDriverWait(self.driver,wait_time)

    def setOwner(self,owner):
        self.owner = owner

    def find_element_by_id(self, id_):
        return  self.driver.find_element_by_id(id_)

    def find_elements_by_id(self, id_):
        return self.driver.find_elements_by_id(id_)

    def find_element_by_xpath(self,id_):
        return self.driver.find_element_by_xpath(id_)

    def find_element_by_xpath(self,path):
        self.driver.find_element_by_xpath(path)

    def open(self):
        pass

    def close(self):
        pass


class IndexView(View):
    def __init__(self,driver):
        super(IndexView,self).__init__(driver)


    def openSearchView(self,keywrod):
        searchView = SearchView(self.driver)
        searchView.search(keywrod)

class SearchView(View):

    def __init__(self,driver):
        super(SearchView,self).__init__(driver,self)

    def sh(self, command):
        # https://blog.csdn.net/qq_42470033/article/details/89456878
        import subprocess
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)



    def search(self,keyword):

        print("点击首页右上方的搜索按钮..")
        resid = "com.ss.android.ugc.aweme:id/bxp"
        if self.wait.until(lambda x:x.find_element_by_id(resid)):
            print("found search button.")
            self.driver.find_element_by_id(resid).click()
            print("-----------------0")

        t = time.time()
        print("查找搜索界面上的输入框.")
        resid = "com.ss.android.ugc.aweme:id/ai2"
        if self.wait.until(lambda x:x.find_element_by_id(resid)):
            edit_text = self.driver.find_element_by_id(resid)
            edit_text.click()
            time.sleep(0.4)
            edit_text.send_keys(keyword)
            time.sleep(0.3)
            edit_text.click()
            time.sleep(0.2)
            print("-----------------4")
            # self.sh("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")

            # 一下两句实现回车搜索
            self.driver.keyevent(66)
            self.driver.press_keycode(66)
            print("-----------------5")

            #粉丝
            print("查找用户信息上的粉丝文本并点击.")
            resid = "com.ss.android.ugc.aweme:id/fq7"
            if self.wait.until(lambda x: x.find_element_by_id(resid)):
                print("-----------------1")
                self.driver.find_element_by_id(resid).click()

                print("查找用户信息界面右上角三个小圆点按钮.")
                resid = "com.ss.android.ugc.aweme:id/f9a"
                if self.wait.until(lambda x: x.find_element_by_id(resid)):
                    print("-----------------1")
                    self.driver.find_element_by_id(resid).click()

                    print("查找发私信按钮.")
                    resid = "com.ss.android.ugc.aweme:id/eiy"
                    if self.wait.until(lambda x: x.find_element_by_id(resid)):
                        print("-----------------1")
                        self.driver.find_element_by_id(resid).click()

                        # print("查找发私信按钮.")
                        # resid = "com.ss.android.ugc.aweme:id/eiy"
                        # if self.wait.until(lambda x: x.find_element_by_id(resid)):
                        #     print("-----------------1")
                        #     self.driver.find_element_by_id(resid).click()

                        resid = "android.widget.EditText[@text='发送消息…']"
                        if self.wait.until(lambda x: x.find_element_by_xpath(resid)):
                            print("-----------------1")
                            edit_text = self.driver.find_element_by_xpath(resid)
                            edit_text.click()
                            edit_text.send_keys("士大夫")




        # if WebDriverWait(self.driver,15).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/bxp")):
        #     self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/bxp").click()

        # d = webdriver.Remote()
        # d.find_element_by_xpath()





if __name__ == '__main__':
    try:
        driver = get_driver('127.0.0.1:62001', 62001)
        # arr = driver.available_ime_engines
        view = IndexView(driver)
        view.openSearchView("1169821489")
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