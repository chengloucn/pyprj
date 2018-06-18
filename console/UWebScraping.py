

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


ulr_data = 'https://coinmarketcap.com/all/views/all/'
# print(ulr_data)

# openning up connection, grabbing the data
uClient = uReq(ulr_data)
page_html = uClient.read()
# print(page_html)
uClient.close()
# 
# html parsing
page_soup = soup(page_html, "html.parser")
# print(page_soup)

#grabs  echa product
all_cryptocurrencies_names = page_soup.findAll("td",{"class":"text-left col-symbol"})
print(len(all_cryptocurrencies_names))
# print(all_cryptocurrencies_names[0])

all_cryptocurrencies_vlues = page_soup.findAll("td",{"class":"no-wrap market-cap text-right"})
print(len(all_cryptocurrencies_vlues))
# print(all_cryptocurrencies_vlues[0])

coin_name_list = []
coin_value_list = []

for coin_name in all_cryptocurrencies_names:
	name = coin_name.text
	coin_name_list.append(name)
	
	# coin_1H = page_soup.findAll("td",{"data-timespan":"1h","data-symbol":name})
	# print(coin_1H)
	# if(len(coin_1H) > 0):
	# 	print(coin_1H[0].text)

for coin_value in all_cryptocurrencies_vlues:
	value = coin_value.text
	value = value.lstrip('\n')
	value = value.lstrip(' ')
	value = value.lstrip('$')
	value = value.rstrip('\n')
	coin_value_list.append(value)

print(len(coin_name_list))
print(len(coin_value_list))


for i in range(len(coin_name_list)):
	print(i,coin_name_list[i],coin_value_list[i])

print('Done')
