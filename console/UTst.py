#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/6/27-22:33
# @desc



# 一个以太坊地址工具箱
#     1. ETH地址生成
#     2. 私钥加解密，私钥查询ETH地址
#     3. 私钥批量加解密功能
#     4. 批量查询ETH地址余额（待开发）
#     5. 批量转账（待开发）
#     单个，批量



import sys
import logging
import re
import hashlib
import urllib.request
import traceback
import requests
import json
from requests.exceptions import Timeout
import progressbar
import random
import subprocess, datetime, os, time
import requests
import chardet




def sleep_progress(sec, msg):
    widgets = [msg, ' [', progressbar.RotatingMarker(), '] ', progressbar.Percentage()]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=100).start()
    for i in range(100):
        time.sleep(sec/100)
        bar.update(i)
    bar.finish()


if __name__ == '__main__':
    sleep_progress(100, 'alex')



