# 创建测试类
import json
import time
import unittest

import logging


from parameterized import parameterized



# 读取数据构造数据返回
import utils
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil


def build_login_data():
    # 创建数据列表
    test_list=[]
    # 读取数构造数据列表
    json_data=utils.load_test_data("login.json")
    test_data = json_data.get("test_login")
    for data in test_data:
        test_list.append((data.get("username"),
                          data.get("pwd"),
                          data.get("code"),
                          data.get("expect")))
    logging.info(test_list)
# 返回数据列表
    return test_list


# 测试类
class TestLogin(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        # 获取用例页面
        cls.index_proxy = IndexProxy()
        cls.login_proxy = LoginProxy()

    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")
        # 点击进入登录页
        self.index_proxy.to_login_page()

    def tearDown(self):
        # 用例执行完毕后等待两秒
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 测试方法,断言
    # 参数化-数据驱动
    @parameterized.expand(build_login_data())
    def test_login(self,username,pwd,code,expect):
        logging.info("username:{},pwd:{},code:{},expect:{}".format(username, pwd, code, expect))
        # 登录
        self.login_proxy.login(username, pwd, code)
        # 断言

        time.sleep(2)
        self.assertIn(expect, self.driver.title)

# 参数化,数据驱动
