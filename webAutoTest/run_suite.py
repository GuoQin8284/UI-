import unittest


# 测试套件
from script.test_cart import TestCart
from script.test_login import TestLogin
from script.test_order import TestOrder
from utils import DriverUtil

suite = unittest.TestSuite()

# 添加用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))
suite.addTest(unittest.makeSuite(TestOrder))

# 关闭 退出驱动开关
DriverUtil.set_auto_quit(False)
# 运行
unittest.TextTestRunner().run(suite)

# 打开 退出驱动开关
DriverUtil.set_auto_quit(True)
# 退出驱动
DriverUtil.quit_driver()
