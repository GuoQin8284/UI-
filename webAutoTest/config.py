# 项目根目录
# print(os.path.dirname(os.path.abspath(__file__)))
import logging.handlers
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(os.path.dirname(__file__))
# 初始化日志配置
def init_log_config():
    # 获取root日志器
    logger=logging.getLogger()

    # 设置日志级别
    logger.setLevel("info")
    # 创建处理器
    sh = logging.StreamHandler()
    log_path = BASE_DIR+"/log/tpshop.log"
    fh=logging.handlers.TimedRotatingFileHandler(log_path,when="D",interval=1,backupCount=5,encoding="utf-8")
    # 创建格式化器  "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    fmt = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 处理器添加格式化器
    sh.setFormatter(fmt)
    fh.setFormatter(fmt)
    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(fh)
