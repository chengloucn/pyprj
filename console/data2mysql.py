#!/usr/bin/python3
#coding=utf-8

import logging
import sys
import pymysql

ex_name_list = ['OKEx', 'Binance', 'Huobi', 'Bitfinex', 'LBank', 'HitBTC', 'Bit-Z', 'ZB.COM', 'Bibox', 'Bithumb', 'BCEX', 'Upbit', 'TOPBTC', 'EXX', 'Kraken', 'CoinEgg', 'BitForex', 'GDAX', 'Coinsuper', 'BTCC', 'Bitbank', 'OEX', 'Gate.io', 'Allcoin', 'Exrates', 'bitFlyer', 'Bitstamp', 'CoinTiger', 'WEX', 'CoinsBank', 'Exmo', 'RightBTC', 'Hotbit', 'IDAX', 'Bittrex', 'DigiFinex', 'Bitinka', 'HADAX', 'Bits Blockchain', 'Livecoin', 'B2BX', 'Kucoin', 'Poloniex', 'Trade By Trade', 'Fatbtc', 'Simex', 'BtcTrade.im', 'BTCBOX', 'YoBit', 'Coinone', 'Liqui', 'Gemini', 'C2CX', 'Sistemkoin', 'itBit', 'Coinroom', 'fex', 'Tidex', 'xBTCe', 'Omicrex', 'DragonEX', 'OOOBTC', 'Qryptos', 'LATOKEN', 'Korbit', 'IDEX', 'Ethfinex', 'Mercatox', 'Cryptopia', 'Waves Decentralized Exchange', 'MBAex', 'CoinEx', 'GOPAX', 'BTC-Alpha', 'BitBay', 'Vebitcoin', 'Indodax', 'OTCBTC', 'LakeBTC', 'BitMart', 'Coinnest', 'CEX.IO', 'QuadrigaCX', 'Coinhub', 'Zaif', 'Bithesap', 'QBTC', 'Bancor Network', 'Ovis', 'Rfinex', 'Negocie Coins', 'CoinEx Market', 'CoinExchange', 'ChaoEX', 'Coindeal', 'COSS', 'LocalTrade', 'Iquant', 'Zebpay', 'BTCTurk', 'Paribu', 'Cryptonex', 'DSX', 'Koineks', 'BX Thailand', 'BitFlip', 'Luno', 'BTC Markets', 'OasisDEX', 'BitShares Asset Exchange', 'Quoine', 'InfinityCoin Exchange', 'Coinsquare', 'Bitso', 'CryptoBridge', 'BL3P', 'Bitbns', 'C-CEX', 'Neraex', 'TDAX', 'Tidebit', 'LiteBit.eu', 'Radar Relay', 'Bitonic', 'Fargobase', 'Independent Reserve', 'Coinfloor', 'RippleFox', 'The Rock Trading', 'Gatehub', 'Koinex', 'Coinbe', 'Mercado Bitcoin', 'CoinMate', 'Stellar Decentralized Exchange', 'BitcoinTrade', 'BitMarket', 'OKCoin International', 'DDEX', 'Stocks.Exchange', 'Bleutrade', 'TradeOgre', 'Switcheo Network', 'Kuna', 'OpenLedger DEX', 'ezBtc', 'Crex24', 'Foxbit', 'AidosMarket', 'Gatecoin', 'Bittylicious', 'CoinFalcon', 'Bitsane', 'Braziliex', 'Koinim', 'Coinut', 'BitcoinToYou', 'CoinCorner', 'Stellarport', 'BTC Trade UA', 'Altcoin Trader', 'Trade Satoshi', 'Ripple China', 'Cryptohub', 'Kyber Network', 'CRXzone', 'SouthXchange', 'Nocks', 'ACX', 'Nanex', 'Bitstamp (Ripple Gateway)', 'CryptoMarket', 'EtherDelta (ForkDelta)', 'Bit2C', 'RuDEX', 'Buda', 'Tripe Dice Exchange', 'Paymium', 'OKCoin.cn', 'Bitmaszyna', 'Bitlish', 'FreiExchange', 'Cryptomate', 'Bisq', 'TCC Exchange', 'Coinrate', 'Cryptox', 'Bitex.la', 'Coingi', 'GuldenTrader', 'Token Store', 'cfinex', 'Novaexchange', 'BitKonan', 'Ore.Bz', 'C-Patex', 'Tux Exchange', 'BarterDEX', 'Octaex', 'ExcambrioRex', 'Stronghold', 'LEOxChange', 'ISX', 'Heat Wallet', 'Dgtmarket']

# 打开数据库连接  涉及中文操作需要指定编码
db_conn = pymysql.connect(host='localhost', user='stockradar', password='alex2018', db='MYSQL', charset='utf8') 
# 使用 cursor() 方法创建一个游标对象 cursor
db_cursor = db_conn.cursor() 

db_sql = "select * from coinradar.focuscoin "
create_table_sql = "create table coinradar.exchange(exname varchar(255) unique ) " 
insert_table_sql = "insert into coinradar.exchange(exname) values('OKEx') " 

# 带参数的SQL语句
insert_table_list_sql = "insert into coinradar.exchange(exname) values('{exchange_name}') " 
query_table_sql = "select * from coinradar.exchange " 
delete_table_sql = "delete from coinradar.exchange " 
drop_table_sql = "drop table coinradar.exchange "

# insert exchange data into db
row_cnt = db_cursor.execute(query_table_sql)
print("db row number %d" %row_cnt)
if row_cnt != 0:
    db_cursor.execute(delete_table_sql)	# 存在数据直接全部删除
    db_conn.commit()

for ind in range(len(ex_name_list)):
	# 带参数SQL，参数的填充
	db_cursor.execute(insert_table_list_sql.format(exchange_name=ex_name_list[ind]))
db_conn.commit()
# 执行SQL查询语句，确认插入数据完整性
row_db_cnt = db_cursor.execute(query_table_sql)
if(row_cnt == row_db_cnt):
	print('insert db cnt success, db count: %d' % len(ex_name_list))
else:
	print('insert db cnt failed, db count: %d, list count: %d' % (row_db_cnt, row_db_cnt))

# 查询数据库，输出表记录
row_cnt = db_cursor.execute(query_table_sql)
row_tuple = db_cursor.fetchall()
print("db data:", row_tuple)
# for ind in range(len(row_tuple)):
#     print("db row %d data: %s" %(ind+1,row_tuple[ind]))
# tuple 元组 如何直接输出有效值？？？？？


# 提交修改
#db_conn.commit()
# 发生错误时回滚
#db_conn.rollback()


# 关闭 cursor
db_cursor.close()

# 关闭数据库连接
db_conn.close()

