# 对象库层
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 业务元素定位信息
        # 复选框-全选框
        self.check_all = (By.XPATH,'//*[@id="ng-app"]/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]/label/input')
        # 超链接-去结算
        self.go_balance = (By.LINK_TEXT,"去结算")


    # 定位全选框复选框
    def find_check_all(self):
        return self.find_element(self.check_all)

    # 定位去结算超链接
    def find_go_balance(self):
        return self.find_element(self.go_balance)


# 操作层
class CartHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page=CartPage()

    # 点击全选
    def check_all(self):
        # 判断如果没有选中--点击全选
        if not self.page.find_check_all().is_selected():
            self.page.find_check_all().click()

    # 点击去结算
    def click_go_balance(self):
        self.page.find_go_balance().click()


# 业务层
class CartProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.handle=CartHandle()

    # 全选商品去结算
    def go_balance(self):
        # 点击全选
        self.handle.check_all()
        # 点击去结算
        self.handle.click_go_balance()
