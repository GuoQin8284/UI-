import logging
import time
import unittest

from parameterized import parameterized

from 代码模板.webAutoTest.page.cart_page import CartProxy
from 代码模板.webAutoTest.page.index_page import IndexProxy
from 代码模板.webAutoTest.page.my_order_page import MyOrderProxy
from 代码模板.webAutoTest.page.order_page import OrderProxy
from 代码模板.webAutoTest.page.order_pay_page import OrderPayProxy
from 代码模板.webAutoTest.utils import DriverUtil


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

        # 去结算

        # 等待加载收货人信息

        # 提交订单

        # 断言
        pass

    def test02_order_pay(self):
        # 进入我的订单页面

        # 切换窗口

        # 去结算 我的订单页面

        # 切换窗口 订单支付页面

        # 断言
        pass

# 参数化,数据驱动
