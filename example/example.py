#encoding=utf-8
import json
import sys
from datetime import datetime
from sf_express import *

appid = 'your appid'
appkey = 'your appkey'
#apply token
token = apply_access_token(appid=appid,appkey=appkey,transMessageId=datetime.now().strftime('%y%m%d%H%M%S%f'))
try:
	access_token = token['body']['accessToken']
	refresh_token = token['body']['refreshToken']
	print 'apply token successed'
except:
	print 'failed to apply token'
	sys.exit(1)
#query token
token = query_access_token(appid=appid,appkey=appkey,transMessageId=datetime.now().strftime('%y%m%d%H%M%S%f'))
try:
	access_token = token['body']['accessToken']
	refresh_token = token['body']['refreshToken']
	print 'query token successed'
except:
	print 'failed to query token'
	sys.exit(1)
#refresh token
ref_token = refresh_access_token(appid=appid,appkey=appkey,transMessageId=datetime.now().strftime('%y%m%d%H%M%S%f'),access_token=access_token,refresh_token=refresh_token)
try:
	access_token = token['body']['accessToken']
	refresh_token = token['body']['refreshToken']
	print 'refresh token successed'
except:
	print 'failed to refresh token'
	sys.exit(1)
#filter order
sf_req = {
	'transMessageId'	:	datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'		:	access_token,
	'refresh_token'		:	refresh_token,
	'filterType'		:	'1',
	'consigneeAddress'	:	'东方路985号18A',
	'consigneeProvince'	:	'上海市',
	'consigneeCity'		:	'上海市',
	'consigneeCounty'	:	'浦东新区',
	'consigneeCountry'	:	'中国',
}
filter_res = filter_order(appid=appid,appkey=appkey,**sf_req)
print 'filter order result:\n',filter_res
#create order
order_id = datetime.now().strftime('%Y%m%d%H%M%S%f')
sf_req = {
	'transMessageId'	:	datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'		:	access_token,
	'refresh_token'		:	refresh_token,
	'orderId'			:	order_id,
	'expressType'		:	'1',
	'payMethod'			:	'1',
	'custId'			:	'7550010173',
	'consigneeInfo'		:	{
		'company'		:	'个人',
		'contact'		:	'刘先生',
		'tel'			:	'15000000000',
		'province'		:	'北京市',
		'city'			:	'北京市',
		'county'		:	'海淀区',
		'address'		:	'西土城路10号',
	},
	'cargoInfo'			:	{
		'cargo'			:	'食品',
	},
}
create_res = create_order(appid=appid,appkey=appkey,**sf_req)
print 'create order result:\n',create_res
#query result
query_res = query_result(appid=appid,appkey=appkey,transMessageId=datetime.now().strftime('%y%m%d%H%M%S%f'),orderId=order_id,access_token=access_token)
mail_no = query_res['body']['mailNo']
print 'query result:\n',query_res

#route query
sf_req = {
	'transMessageId'	:	datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'		:	access_token,
	'trackingType'		:	'1',
	'trackingNumber'	:	[mail_no],
}
import pdb
pdb.set_trace()
route_query_res = route_query(appid=appid,appkey=appkey,**sf_req)
print 'route query result:\n',route_query_res

#route query inc
sf_req = {
	'transMessageId'	:	datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'		:	access_token,
	'orderId'			:	order_id,
}
route_res = route_query_inc(appid=appid,appkey=appkey,**sf_req)
print 'route query inc result:\n',route_res

#access img
sf_req = {
	'transMessageId'	:	datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'		:	access_token,
	'orderId'			:	order_id,
}
access_img_res = access_order_img(appid=appid,appkey=appkey,**sf_req)
print 'access img result:\n',access_img_res

