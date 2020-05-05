
from model.db_mongo import MongoDB
# from selenium import webdriver
# 注意,手机需要从appium导入
from appium import webdriver

db = MongoDB()

class DYModel():
    def __init__(self):
        self.video_datas = []

    def is_too_much_videos(self):
        return len(self.video_datas) > 5

    def pop_video(self):
        if len(self.video_datas) > 0:
            return self.video_datas.pop(0)
        return None

    def add_video(self,video):
        self.video_datas.append(video)


dy_model = DYModel()


def get_driver(device, port,delay=10):
    # device, port = '127.0.0.1:62001', 62001
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
    driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)
    driver.implicitly_wait(delay)
    return driver
