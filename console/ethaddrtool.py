#!/usr/bin/env python3
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/6/21-17:07
# @desc


from ULogger import *

from ecdsa import SigningKey, SECP256k1
import sha3


# pip install ecdsa
# pip install pysha3


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


from ecdsa import SigningKey, SECP256k1
import sha3


# ecdsa 签名、验证
# create keypairs (signing key and verifying key), sign messages, and verify the signatures.

# 库 hashlib，sha3
# hashlib 是用于给数据加密的包，内有很多加密方式，包括md5,sha1,sha224,sha256,sha384,sha512等一系列用于加密的算法。
#         提供常见的摘要算法，又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# pysha3：构造hash对象，接口支持生成几类加密算法：SHA3, SHAKE and Keccak算法。

g_logger = ULogger()

# 生产以太坊地址
def genETHAddr():
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()

    keccak.update(pub)
    address = keccak.hexdigest()[24:]

    g_logger.info("Private key: %s" % priv.to_string().hex())
    g_logger.info("Public key: %s"  % pub.hex())
    g_logger.info("Address: 0x%s"  % address)

def main():
    g_logger.info("ethaddrtool main")
    genETHAddr()
    g_logger.info("ethaddrtool end!!")

__all__ = [""]

if __name__ == '__main__':
    main()


