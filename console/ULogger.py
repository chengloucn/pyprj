#! /usr/bin/env python
# coding: utf-8

import os
import logging

class ULogger(logging.Logger):

    logger = None

    def __init__(self, filename=None):
        # super(MyLogger, self).__init__(filename)
        logging.Logger.__init__(self, filename)


        # 设置日志格式
        fmtHandler_console = logging.Formatter('%(message)s')

        fmtHandler = logging.Formatter('#%(levelname)s %(asctime)s #%(message)s')


        # 终端log输出流设置
        try:
            consoleHd = logging.StreamHandler()
            consoleHd.setLevel(logging.DEBUG)
            consoleHd.setFormatter(fmtHandler_console)
            self.addHandler(consoleHd)
        except Exception as reason:
            self.error("%s" % reason)

        if filename:
            # 设置log文件
            try:
                os.makedirs(os.path.dirname(filename))
            except Exception as reason:
                pass
            try:
                fileHd = logging.FileHandler(filename, encoding='utf-8')
                fileHd.setLevel(logging.INFO)
                fileHd.setFormatter(fmtHandler)
                self.addHandler(fileHd)
            except Exception as reason:
                self.error("%s" % reason)

        return

        # # 设置回滚日志,每个日志最大10M,最多备份5个日志
        # try:
        #     rtfHandler = logging.BaseRotatingHandler(
        #                     filename, maxBytes=10*1024*1024, backupCount=5)
        # except Exception as reason:
        #     self.error("%s" % reason)
        # else:
        #     self.addHandler(rtfHandler)

__all__ = ["ULogger"]

def main():
    logfile1 = 'log/test1.log'
    logger1 = ULogger(logfile1)
    logger1.debug("debug msg")
    logger1.info("info msg")
    logger1.warning("warning msg")
    logger1.error("error msg")
    logger1.critical("critical msg")

    logfile2 = 'log/test2.log'
    logger1 = ULogger(logfile2)
    logger1.debug("debug msg")
    logger1.info("info msg")
    logger1.warning("warning msg")
    logger1.error("error msg")
    logger1.critical("critical msg")


__all__ = ["ULogger"]

if __name__ == '__main__':
    main()