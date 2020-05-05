from appium import webdriver

class Simulator():
    def __init__(self,cap):
        self.cap = cap

        self.driver             = webdriver.Remote('http://localhost:4723/wd/hub', cap)
        self.driver.implicitly_wait(10)



if __name__ == '__main__':
    device,port = '127.0.0.1:62001', 62001
    cap = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": device,
        "udid": device,
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
        # 再次启动不需要再次安装
        "noReset": True,
        # unicode键盘 我们可以输入中文
        'unicodekeyboard': True,  # 使用unicode输入法
        # 操作之后还原回原先的输入法
        'resetkeyboard': True,  # 还原输入法
    }
    simulator = Simulator(cap)


