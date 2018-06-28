#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/6/27-22:33
# @desc


import argparse

parser = argparse.ArgumentParser(description="this is a tst program")
parser.add_argument("echo", help="echo the string")
args = parser.parse_args()
print(args.echo)

