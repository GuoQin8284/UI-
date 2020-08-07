# 对象库层
from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle
from utils import switch_new_window


class OrderPayPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 业务元素定位信息
        # 单选按钮--货到付款
        self.cod = (By.CSS_SELECTOR,"input[value='pay_code=cod']")
        # 超链接--确认支付方式
        self.confirm_pay=(By.LINK_TEXT,"确认支付方式")

    # 定位货到付款单选按钮
    def find_cod(self):
        return self.find_element(self.cod)

    # 定位确认支付方式超链接
    def find_confirm_pay(self):
        return self.find_element(self.confirm_pay)


# 操作层
class OrderPayHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.page = OrderPayPage()

    # 点击货到付款
    def click_cod(self):
        self.page.find_cod().click()

    # 点击确认支付方式
    def click_confirm_pay(self):
        self.page.find_confirm_pay().click()


# 业务层
class OrderPayProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.handle=OrderPayHandle()

    # 确认支付方式
    def confirm_pay_way(self):
        # 点击货到付款款
        switch_new_window()
        self.handle.click_cod()
        # 点击确认支付方式
        self.handle.click_confirm_pay()
