# 创建测试类
import time
import unittest



# 测试类
from 代码模板.webAutoTest.page.index_page import IndexProxy
from 代码模板.webAutoTest.page.login_page import LoginProxy
from 代码模板.webAutoTest.utils import DriverUtil


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
    def test_login(self):
        # 登录
        self.login_proxy.login("13012345678", '123456', '8888')
        # 断言
        time.sleep(2)
        self.assertIn("我的账户", self.driver.title)

# 参数化,数据驱动
