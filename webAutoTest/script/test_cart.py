# 参数化,数据驱动
# 创建测试类
import time
import unittest

from parameterized import parameterized




# 读取数据构造数据返回
from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from utils import DriverUtil


def build_cart_data():
    # 创建数据列表

    # 读取数构造数据列表

    # 返回数据列表
    pass


class TestCart(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        # 获取用例页面
        cls.index_proxy = IndexProxy()
        cls.goods_search_proxy = GoodsSearchProxy()
        cls.goods_detail_proxy = GoodsDetailProxy()

    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")

    def tearDown(self):
        # 用例执行完毕后等待两秒
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 创建测试方法,断言
    # 参数化-数据驱动
    def test_cart(self):
        # 搜索指定商品
        self.index_proxy.search_goods('小米')
        # 进入商品详情页面
        self.goods_search_proxy.to_goods_detail_page('小米')
        # 加入购物车
        self.goods_detail_proxy.join_cart()
        time.sleep(2)

        # 断言
        # 注意点 -- 如果定位失败了怎么排查问题
        is_success = self.goods_detail_proxy.is_join_cart_success("添加成功")
        self.assertTrue(is_success)
# 参数化,数据驱动
