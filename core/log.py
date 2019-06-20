import logzero
from logzero import logger


class Log():
    def __init__(self, name):
        # 配置文件 是否生成log文件
        if True:
            logzero.logfile("./" + name + ".log", maxBytes=1e6, backupCount=1)

    def write(self, content):
        logger.info(content)
