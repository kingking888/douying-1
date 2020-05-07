
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ViewHelper():
    def __init__(self,driver,wait_time=10):
        self.driver     = driver
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
        except Exception as e:
            ele = None
            print(e)

        self.dicEle[id_] = ele
        return  ele

    def find_elements_by_id(self, id_):
        return self.driver.find_elements_by_id(id_)

    def find_element_by_class_name(self, id_, message='',use_timeout=True,force_find=False):
        ele = self.dicEle.get(id_)
        if ele and ele.is_displayed() and force_find == False:
            return ele

        try:
            if use_timeout > 0:
                ele = self.wait.until(lambda x: x.find_element_by_class_name(id_), message=message)
            else:
                ele = self.driver.find_element_by_class_name(id_)
        except Exception as e:
            ele = None
            print(e)

        self.dicEle[id_] = ele
        return ele


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

    # by_:@see By.xxx,e.g. By.ID
    def click(self,id_,by_=By.ID,message=''):
        ele = None
        try:
            ele = self.wait.until(EC.element_to_be_clickable((by_, id_)), message=message)
            if ele:
                ele.click()
            else:
                print("cant get a element to click by id:%s" % id_)

            self.dicEle[id_] = ele
        except Exception as e:
            print("error cant get a element to click by id:%s" % id_)

        return ele
