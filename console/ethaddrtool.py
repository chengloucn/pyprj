#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/6/21-17:07
# @desc


from ULogger import *



# 参考 ethaddr_utils.py
#
# 区块链钱包：一个工具，帮忙生成私钥、公钥、生成符合某个公链规范的地址（不同的公链有不同的算法规范）。
# 地址生成过程：大的流程是：私钥 -->> 公钥 -->> 地址。
# 1）私钥是一个256位随机数。
# 2）椭圆曲线算公钥。
# 3）对公钥哈希技术。
# 4）计算 RIPEMD-160哈希值。
# 5）加入地址版本号。
# 6）计算 SHA-256 哈希值。
# 7）效验位。
# 8）用Base58编码变换地址。




def main():
    logger1 = ULogger()
    logger1.info("ethaddrtool main")

    logger1.info("ethaddrtool end!!")

__all__ = [""]

if __name__ == '__main__':
    main()


