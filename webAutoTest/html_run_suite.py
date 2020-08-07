import unittest

import time




# 测试套件
from 代码模板.webAutoTest import config
from 代码模板.webAutoTest.script.test_login import TestLogin
from 代码模板.webAutoTest.tools.HTMLTestRunner import HTMLTestRunner

from 代码模板.webAutoTest.utils import DriverUtil

suite = unittest.TestSuite()

# 添加用例
suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestCart))
# suite.addTest(unittest.makeSuite(TestOrder))

# 关闭 退出驱动开关
DriverUtil.set_auto_quit(False)
# 运行


with open(config.BASE_DIR+"/report/tpshop自动化测试报告{}.html".format(time.strftime("%Y%m%d%H%M%S")),"wb") as f:
    HTMLTestRunner(f,title="tpshop商城自动化测试报告",description="win10.Chrome").run(suite)



# unittest.TextTestRunner().run(suite)
# 使用HTMLTestRunner运行器


# 打开 退出驱动开关
DriverUtil.set_auto_quit(True)
# 退出驱动
DriverUtil.quit_driver()
