#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/8/7-15:57
# @desc

import sys
sys.path.append('.')  # 项目根目录

from console.ULogger import ULogger

g_logger = ULogger()
g_logger.setLevel('INFO')

import hashlib
import base64

# ord()把ASCII转换成数字。
# chr()则相反，把数字转换成ASCII。

'''
加解密算法：加密内容和密钥组成新字符串，其中掺入了无意义沙子。
'''

# key为密钥，org_str为需要加密的字符串
def Encode(key, org_str):
    md_hash = hashlib.md5()
    md_hash.update(org_str.encode())
    md_str = org_str + md_hash.hexdigest()[:6]  # 数字摘要 16进制HASH

    enc = []
    for i in range(len(md_str)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(md_str[i]) + ord(key_c)) % 256)
        enc.append(enc_c)

    # 对字符串进行编码
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# key为密钥，enc_str为已经加密了的字符串
def Decode(key, enc_str):
    if len(enc_str) == 64:  ## 长度64位不加解密
        return enc_str
    dec = []
    enc = base64.urlsafe_b64decode(enc_str).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)

    md_clear = "".join(dec)

    return md_clear[:-6]


if __name__ == '__main__':
    g_logger.info("begin")

    KEYSTR = 'mima123456'
    ORG_STR = "wo yao jia mi de zi fu chuang"

    g_logger.info("key: %s", KEYSTR)
    enc_str = base64.urlsafe_b64encode(KEYSTR.encode())
    enc_str_dec = base64.urlsafe_b64encode(KEYSTR.encode()).decode()
    g_logger.info("key encode: %s", enc_str )
    g_logger.info("key encode decode: %s", enc_str_dec )

    g_logger.info("key decode: %s", base64.urlsafe_b64decode(enc_str_dec) )
    g_logger.info("key encode decode: %s", base64.urlsafe_b64decode(enc_str_dec).decode() )

    g_logger.info("key: %s", KEYSTR)
    enc_str = Encode(KEYSTR, ORG_STR)
    dec_str = Decode(KEYSTR, enc_str)
    g_logger.info("org_str: %s ------- dec_str: %s", ORG_STR, dec_str)

    g_logger.info("end")

