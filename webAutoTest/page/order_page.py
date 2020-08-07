import time
from selenium.webdriver.common.by import By




# 对象库层
from base.base_page import BasePage, BaseHandle


class OrderPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 业务元素定位信息
        # 超链接--提交订单
        self.submit_order = (By.XPATH,'//*[@id="cart2_form"]/div/div[2]/div[2]/div/a/span')

    # 定位提交订单超链接
    def find_submit_order(self):
        return self.find_element(self.submit_order)


# 操作层
class OrderHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page=OrderPage()

    # 点击提交订单超链接
    def click_submit_order(self):
        self.page.find_submit_order().click()


# 业务层
class OrderProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.handle=OrderHandle()

    # 提交订单
    def submit_order(self):
        # 点击提交订单超
        time.sleep(4)
        self.handle.click_submit_order()
