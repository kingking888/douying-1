import os

#os.system('mitmdump -s decode_douyin.py -p 8080')
import time
import random
from appium import webdriver
# 等待元素加载
from selenium.webdriver.support.ui import WebDriverWait

fansId_1 = "191433445"
fansId_2 = "2156323738"
fansId = fansId_2

# 定义设备参数
cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
    # 再次启动不需要再次安装
    "noReset": True,
    # unicode键盘 我们可以输入中文
    'unicodekeyboard': True,  # 使用unicode输入法
    # 操作之后还原回原先的输入法
    'resetkeyboard': True,  # 还原输入法
}


def handle_appium(device,port):
    cap = {
        "platformName"      : "Android",
        "platformVersion"   : "5.1.1",
        "deviceName"        : device,
        "udid"              : device,
        "appPackage"        : "com.ss.android.ugc.aweme",
        "appActivity"       : "com.ss.android.ugc.aweme.main.MainActivity",
        # 再次启动不需要再次安装
        "noReset"           : True,
        # unicode键盘 我们可以输入中文
        'unicodekeyboard'   : True,  # 使用unicode输入法
        # 操作之后还原回原先的输入法
        'resetkeyboard'     : True,  # 还原输入法
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)

    def get_size():
        # 获取设备屏幕大小
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return x, y

    # 点击搜索框
    try:
        path = "com.ss.android.ugc.aweme:id/bx4"
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(path)):
            driver.find_element_by_id(path).click()
    except:
        pass

    # 定位搜索框
    try:
        path = "//android.widget.EditText[@resource-id='com.ss.android.ugc.aweme:id/ai2']"
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(path)):
            driver.find_element_by_xpath(path).send_keys(fansId)  # 2156323738
    except:
        pass

    # 点击搜索
    try:
        path = "//android.widget.ImageView[@resource-id='com.ss.android.ugc.aweme:id/c4y']"
        path = 'com.ss.android.ugc.aweme:id/c4y'
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(path)):
            driver.find_element_by_id(path).click()
    except:
        driver.tap([(104, 80), (152, 128)])

    # 点击下拉第一个
    path = 'com.ss.android.ugc.aweme:id/c52'
    try:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(path)):
            driver.find_element_by_id(path).click()
    except:
        driver.tap([(32, 184), (80, 232)], 500)

    # 点击用户,进入个人主页
    path = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.views.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/android.views.View[1]/android.widget.ImageView"  # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.views.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.views.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView[2]"
    path = "com.ss.android.ugc.aweme:id/fn9"  # 粉丝数量
    if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(path)):
        driver.find_element_by_id(path).click()

    # 点击粉丝
    if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@text='粉丝']")):
        driver.find_element_by_xpath("//android.widget.TextView[@text='粉丝']").click()
    # path = "android.widget.TextView[@text='粉丝']"
    # if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath(path)):
    #   driver.find_element_by_xpath(path).click()

    # 等待页面刷新
    time.sleep(3)

    # 开始滑动
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.9)
    y2 = int(l[1] * 0.25)

    def getRange(min, max):
        return random.random() * (max - min) + min

    while True:
        if '没有更多了' in driver.page_source:
            break
        elif "TA还没有粉丝" in driver.page_source:
            break
        else:
            # 初始位置x1,y1   结束位置为:x1,y2
            driver.swipe(x1, y1, x1, y2)
            time.sleep(getRange(0.5, 5))





if __name__ == "__main__":
    m_list = []
    devices_list = ['127.0.0.1:62001',"127.0.0.1:62025"]

    handle_appium('127.0.0.1:62001',62001)

