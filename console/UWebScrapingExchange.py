

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import logging
import sys

# 获取 logger 实例，如果参数为空则返回 root logger
logger = logging.getLogger() 
# 指定 logger 输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-6s %(message)s')
# 文件日志
file_handler = logging.FileHandler('appdev.log')
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
# 为 logger 添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# 指定日志的最低输出级别，默认为 WARN级别
logger.setLevel(logging.DEBUG)
logging.info('logging initialization')

ulr_data = 'https://coinmarketcap.com/exchanges/volume/24-hour/'
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
all_exchange_names = page_soup.findAll("h3",{"class":"padding-top--lv6 margin-bottom--lv2"})
logging.info('Get Exchange names number：%d',len(all_exchange_names))
all_exchange_vols = page_soup.findAll("td",{"class":"text-bold text-right volume"})
logging.info('Get Exchange volumes number：%d',len(all_exchange_vols))

# ?????????
# 交易所、成交量，两者数据个数不一致 ??? 高效解析网页数据？？

ex_name_list = []
ex_vol_list = []
for i in range(len(all_exchange_names)):
	name = all_exchange_names[i].a.text
	ex_name_list.append(name)
for i in range(len(all_exchange_vols)):	
	vol = all_exchange_vols[i].text
	ex_vol_list.append(vol)

# 打印出 前30位 交易所名称，及成交量
for ind in range(30):
	logging.info('exchanges name %s, volume %s',ex_name_list[ind],ex_vol_list[ind])
