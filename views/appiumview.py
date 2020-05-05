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

        print("click search button.")
        resid = "com.ss.android.ugc.aweme:id/bxp"
        if self.wait.until(lambda x:x.find_element_by_id(resid)):
            print("found search button.")
            self.driver.find_element_by_id(resid).click()
            print("-----------------0")

        t = time.time()
        print("set search text.")
        resid = "com.ss.android.ugc.aweme:id/ai2"
        if self.wait.until(lambda x:x.find_element_by_id(resid)):
            print("-----------------1")
            edit_text = self.driver.find_element_by_id(resid)
            edit_text.click()
            print("-----------------2")
            time.sleep(1)
            edit_text.send_keys(keyword)
            print("-----------------3")
            time.sleep(1)
            edit_text.click()
            time.sleep(1)
            print("-----------------4")
            # self.sh("adb shell ime set com.sohu.inputmethod.sogou/.SogouIME")
            time.sleep(1)

            # 一下两句实现回车搜索
            self.driver.keyevent(66)
            self.driver.press_keycode(66)
            print("-----------------5")

            resid = "com.ss.android.ugc.aweme:id/fq7"
            if self.wait.until(lambda x: x.find_element_by_id(resid)):
                print("-----------------1")
                self.driver.find_element_by_id(resid).click()




        # if WebDriverWait(self.driver,15).until(lambda x:x.find_element_by_id("com.ss.android.ugc.aweme:id/bxp")):
        #     self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/bxp").click()

        # d = webdriver.Remote()
        # d.find_element_by_xpath()





if __name__ == '__main__':
    try:
        driver = get_driver('127.0.0.1:62001', 62001)
        # arr = driver.available_ime_engines
        view = IndexView(driver)
        view.openSearchView("减肥")
        time.sleep(10000)
        driver.close()
    except Exception as e:
        print(e)
        driver.close()

    # driver.press_keycode(66)
    #  d = webdriver.Remote()

    # d.close()
    # d.keyevent()