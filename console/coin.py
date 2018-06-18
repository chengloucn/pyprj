#!/usr/bin/env python
# encoding: utf-8

# @author   :chenglou
# @contact  :chenglou0710@126.com
# @time     :2018/5/17-17:57
# @desc     :

import os
import sys
import json
import requests
import tempfile
import requests_cache

class Market(object):
    _session = None
    __DEFAULT_BASE_URL = u'https://api.coinmarketcap.com/v2/'
    __DEFAULT_TIMEOUT = 30
    __TEMPDIR_CACHE = True

    def __init__(self, base_url = __DEFAULT_BASE_URL, request_timeout = __DEFAULT_TIMEOUT, tempdir_cache = __TEMPDIR_CACHE):
        self.base_url = base_url
        self.request_timeout = request_timeout
        self.cache_filename = 'coinmarketcap_cache'
        self.cache_name = os.path.join(tempfile.gettempdir(), self.cache_filename) if tempdir_cache else self.cache_filename

    @property
    def session(self):
        if not self._session:
            self._session = requests_cache.core.CachedSession(cache_name=self.cache_name, backend='sqlite', expire_after=120)
            self._session.headers.update({'Content-Type': 'application/json'})
            self._session.headers.update({'User-agent': 'coinmarketcap - python wrapper around \
                                         coinmarketcap.com (github.com/barnumbirr/coinmarketcap)'})
        return self._session

    def __request(self, endpoint, params):
        response_object = self.session.get(self.base_url + endpoint, params = params, timeout = self.request_timeout)

        try:
            response = json.loads(response_object.text)

            if isinstance(response, list) and response_object.status_code == 200:
                response = [dict(item, **{u'cached':response_object.from_cache}) for item in response]
            if isinstance(response, dict) and response_object.status_code == 200:
                response[u'cached'] = response_object.from_cache

        except Exception as e:
            return e

        return response

    def listings(self):
        response = self.__request('listings/', params=None)
        return response

    def ticker(self, currency="", **kwargs):
        params = {}
        params.update(kwargs)

        if currency:
            currency = str(currency) + '/'

        response = self.__request('ticker/' + currency, params)
        return response

    def stats(self, **kwargs):
        params = {}
        params.update(kwargs)
        response = self.__request('global/', params)
        return response


# 列出所有加密货币种类
def list_all_coin(market_inst):
    dict_list = coin_market.listings()
    dict_list = dict_list.get('data')
    print(u'加密货币种类：',len(dict_list))

    # in_json = json.dumps(dict_list)
    # print('JSON:', in_json)

    for i in range(len(dict_list)):
        # print("序号：%s   值：%s" % (i + 1, dict_list[i]))
        coin_dict_item = dict_list[i]
        # print('id: %d, name:%s, symbol %s, website_slug %s',
        #       coin_dict_item.get('id'),
        #       coin_dict_item.get('name'),
        #       coin_dict_item.get('symbol'),
        #       coin_dict_item.get('website_slug'))
        print("%s" % coin_dict_item.get('symbol'))




if __name__ == '__main__':
    coin_market = Market()

    # 列出所有加密货币种类
    list_all_coin(coin_market)






