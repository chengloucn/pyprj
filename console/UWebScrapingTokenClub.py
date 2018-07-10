#!/usr/bin/env python3
# encoding: utf-8


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import logging
import sys
import json

# 获取 logger 实例，如果参数为空则返回 root logger
logger = logging.getLogger() 
# 指定 logger 输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-6s %(message)s')
# 文件日志
file_handler = logging.FileHandler('appdev.log', encoding = "UTF-8")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
# 为 logger 添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# 指定日志的最低输出级别，默认为 WARN级别
logger.setLevel(logging.INFO)
logging.info('logging initialization')

ulr_data = 'https://api.schail.com/v1/concept/all-list'
logging.info(ulr_data)


# openning up connection, grabbing the data
uClient = uReq(ulr_data)
page_html = uClient.read()
logging.info('Get WebPageData Len：%d',len(page_html))
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
logging.info('Get BeautifulSoup Data Len：%d',len(page_soup))

# parse data
# 网页数据 BeautifulSoup 的处理，字符串与json数据的转化
data_str = page_soup.text
js_list = json.loads(data_str)

data_list = js_list['data']['list']
logging.info("网页获取数据长度： %d" %(len(data_list)))


class CoinData():
    def __init__(self, name, symbol, change24h, marketcap):
        self.coin_tickerNameCh = name
        self.coin_tickerSymbol = symbol
        self.coin_change24h = change24h        
        self.coin_marketcap = marketcap


class BkData():
    def __init__(self, name, change24h, marketcap, tick_list):
        self.bk_name = name
        self.bk_change24h = change24h        
        self.bk_marketcap = marketcap
        self.bk_tickerList = []


       # logging.debug(self.bk_name, self.bk_change24h, self.bk_marketcap, tick_list)
        for ind in range(len(tick_list)):
            coin_inst = CoinData(tick_list[ind]['tickerNameCh'], tick_list[ind]['tickerSymbol'], tick_list[ind]['change24h'], tick_list[ind]['marketcap'])
            self.bk_tickerList.append(coin_inst)



bkdata_list = []
for ind in range(len(data_list)):
    bk_inst = BkData(data_list[ind]['name'], data_list[ind]['change24h'], data_list[ind]['marketcap'], data_list[ind]['tickerList'])
    bkdata_list.append(bk_inst)


# 输出 板块，24小时涨跌幅，成交量数据
logging.info("板块数量 %d" %(len(bkdata_list)))
coin_num = 0
for ind in range(len(bkdata_list)):
    logging.info("板块名称:%s, 24H涨跌幅:%s, 成交量:%s" %(bkdata_list[ind].bk_name, bkdata_list[ind].bk_change24h, bkdata_list[ind].bk_marketcap))
    coin_num += len(bkdata_list[ind].bk_tickerList)


    for j in range(len(bkdata_list[ind].bk_tickerList)):
        coin_datainst = bkdata_list[ind].bk_tickerList[j]
        logging.info("     代币符号:%s, 24H涨跌幅:%s, 成交量:%s, 全称:%s" %(coin_datainst.coin_tickerSymbol,
			coin_datainst.coin_change24h, coin_datainst.coin_marketcap, coin_datainst.coin_tickerNameCh) )

logging.info("代币数量 %d" %(coin_num))


logging.info('Program end!!!')





