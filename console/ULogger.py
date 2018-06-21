#! /usr/bin/env python
# coding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/5/3-15:06
# @desc     :

import os
import logging
import sys

class ULogger(logging.Logger):

    def __init__(self, filename=None):
        logging.Logger.__init__(self, filename)

        # 获取 logger 实例，如果参数为空则返回 root logger
        logger = logging.getLogger()
        # 指定 logger 输出格式
        formatter = logging.Formatter('#%(asctime)s %(levelname)-6s %(message)s#')

        # 文件日志
        if filename:
            log_path = os.path.abspath('..')
            log_path = os.path.join(log_path, "log")
            log_path = os.path.join(log_path, filename)
            file_handler = logging.FileHandler(log_path)
            file_handler.setFormatter(formatter)

        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter

        # 为 logger 添加的日志处理器
        self.addHandler(console_handler)
        if filename:
            self.addHandler(file_handler)

        # 指定日志的最低输出级别，默认为 WARN级别
        self.setLevel(logging.DEBUG)
        logging.info('logging initialization')

        return


__all__ = ["ULogger"]

def main():
    logger1 = ULogger()
    logger1.debug("logger1 debug msg")
    logger1.info("logger1 info msg")
    logger1.warning("logger1 warning msg")
    logger1.error("logger1 error msg")
    logger1.critical("logger1 critical msg")

    logfile2 = 'test2.log'
    logger2 = ULogger(logfile2)
    logger2.debug("logger2 debug msg")
    logger2.info("logger2 info msg")
    logger2.warning("logger2 warning msg")
    logger2.error("logger2 error msg")
    logger2.critical("logger2 critical msg")


__all__ = ["ULogger"]

if __name__ == '__main__':
    main()