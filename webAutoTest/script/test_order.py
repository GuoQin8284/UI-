import logging
import time
import unittest

from parameterized import parameterized




# 读取数据构造数据返回
from page.cart_page import CartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_page import OrderProxy
from page.order_pay_page import OrderPayProxy
from utils import DriverUtil, exist_text, switch_new_window


def build_order_data():
    # 创建数据列表

    # 读取数构造数据列表

    # 返回数据列表
    pass


def build_order_pay_data():
    # 创建数据列表

    # 读取数构造数据列表

    # 返回数据列表
    pass


class TestOrder(unittest.TestCase):
    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        # 获取用例页面
        cls.index_proxy = IndexProxy()
        cls.cart_proxy = CartProxy()
        cls.order_proxy = OrderProxy()
        cls.myorder_proxy = MyOrderProxy()
        cls.orderpay_proxy = OrderPayProxy()

    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")

    def tearDown(self):
        # 用例执行完毕后等待两秒
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    def test01_order(self):
        # 进入购物车页面
        self.index_proxy.to_cart_page()
        # 去结算
        self.cart_proxy.go_balance()
        # 等待加载收货人信息
        # time.sleep(3)
        # 提交订单
        self.order_proxy.submit_order()
        # 断言
        is_exist=exist_text("订单提交成功，请您尽快付款")
        self.assertTrue(is_exist)


    def test02_order_pay(self):
        # 进入我的订单页面
        self.index_proxy.to_my_order_page()
        # 切换窗口
        switch_new_window()
        # 去结算 我的订单页面
        self.myorder_proxy.go_pay()
        # 切换窗口 订单支付页面
        switch_new_window()

        # 断言
        self.assertTrue(exist_text("订单提交成功，请您尽快付款"))
