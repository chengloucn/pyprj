#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/5/4-11:06
# @desc     :


import os
import logging
import yaml
from ULogger import ULogger



class UCfgYAML(str):

    cfgfile = None

    def __init__(self, filename=None):
        self.cfgfile = filename

        logger1 = ULogger(filename)

        # 配置文件目录
        cfgpath = os.path.dirname(__file__)
        cfgpath = os.path.abspath(os.path.join(cfgpath, os.path.pardir))
        cfgpath = cfgpath + os.sep + 'conf' + os.sep + 'cfg.yaml'

        logger1.debug("load config file %s",cfgpath)


        # 配置文件加载
        file1 = open(cfgpath, "r", encoding="utf-8")
        filedata = yaml.safe_load(file1)
        logger1.debug("config file data: %s", filedata)


        return


def main():
    cfgfile1 = '../conf/cfg.yaml'
    cfginst = UCfgYAML(cfgfile1)


if __name__ == '__main__':
    main()

