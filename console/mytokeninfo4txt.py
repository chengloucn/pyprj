

import json
file_path = 'mytoken_data.txt'

filep = open(file_path, 'r', encoding='utf-8') 
file_data = filep.read()

status = True
try:
	js_data = json.loads(file_data)
except Exception as ex:
	print(e)
	status = False


if(status):
	# JSON 在python中分别由 list和dict 组成
	# 每种币的信息不一样，有些币种的信息字段缺少，处理时要注意

	print(js_data['data']['symbol'])
	print(js_data['data']['price'])
	print(js_data['data']['blockchain'])
	print(js_data['data']['description'])
	# print(js_data['data']['ico_distribution'])
	#print(js_data['data']['ico_date_display'])
	print(js_data['data']['online_exchange_number'])

	# js_data['data']['info_items']

	for it_info in js_data['data']['info_items']:
		print(it_info['caption'],it_info['content'])

filep.close()













