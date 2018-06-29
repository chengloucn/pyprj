#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/6/28-15:07
# @desc



import argparse
import sys

parser = argparse.ArgumentParser(description="this is a tst program")

# positional arguments 定位参数
parser.add_argument("usrname")

# optional arguments 可选参数
parser.add_argument('-m', dest='mining_mode', action='store_true', help=u'靓号挖掘模式 ')
parser.add_argument('--conf', dest='conf_file', type=str, help=u'指定配置文件名 ')
parser.add_argument('--test-addr', dest='test_addr', type=str, help=u'指定配置文件名 ')
parser.add_argument('-k', dest='key', type=str, help=u'加密/解密密码', default='')

# 互斥参数
group = parser.add_mutually_exclusive_group()
group.add_argument("-v1", "--verbose1", action="store_true")
group.add_argument("-v2", "--verbose2", action="store_true")

args = parser.parse_args()
print(args.usrname)    # 定位参数，可直接参数值

parser.print_help()

