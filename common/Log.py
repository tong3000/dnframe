import logging
import time
from common.util import projjectpath

class framelog():
    def __init__(self, logger=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        # 路径需要修改，为空当前文件夹下
        self.log_path = projjectpath()+"logs\\"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        fh.close()

    # log函数
    def log(self):
        return self.logger


if __name__ == '__main__':
    lo = framelog()
    log = lo.log()
    log.error("error")
    log.debug("debug")
    log.info("info")
    log.critical("严重")
    print(projjectpath())
