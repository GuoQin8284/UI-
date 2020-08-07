import json
import time
from selenium import webdriver



# 工具方法 -- 读取测试数据文件
import config


def load_test_data(file_name):
    # 打开json文件流
    # 读取数据并返回
    with open(config.BASE_DIR+"/data/"+file_name,"r",encoding="utf_8") as f:
        json_data = json.load(f)
        return json_data


# 工具方法 -- 切换到新窗口
def switch_new_window():
    # 等待新窗口加载
    time.sleep(2)
    # 切换到新窗口
    driver= DriverUtil.get_driver()
    driver.switch_to.window(driver.window_handles[-1])

# 工具方法--判断页面是否存在指定文本内容 -- 参数-判断内容 -- 返回布尔结果
def exist_text(text):
    # 定位失败之后会抛出异常,暂停运行所以将代码放入try-except中
    try:
        xpath = "//*[contains(text(),'{}')]".format(text)
        element=DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element is not None
    except Exception as e:
        print("current page is not contains[{}]".format(text))
        return False
# 驱动工具类
# 保证浏览器驱动对象只有一个
class DriverUtil():
    # 定义类属性保存驱动对象
    _driver = None
    # 定义标记,判断是否需要退出驱动对象
    _auto_quit = True

    # 获取浏览器驱动对象  类方法
    @classmethod
    def get_driver(cls):
        # 判断_driver中是否存有驱动,如果没有实例化一个保存在_driver中
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        # 返回_driver中的驱动对象
        return cls._driver

    # 退出浏览器驱动对象 类方法
    @classmethod
    def quit_driver(cls):
        # 如果_driver属性中有驱动对象,退出驱动对象-重置为None
        if cls._auto_quit and cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

    # 手动设置自动退出
    @classmethod
    def set_auto_quit(cls, auto_quit):
        cls._auto_quit=auto_quit
