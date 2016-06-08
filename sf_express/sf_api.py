#!/usr/bin/python
#encoding=utf-8
import httplib
import json
import pdb
from datetime import datetime
import sys


def send_request(url,data):
	headers = {"Content-Type"	:	"application/json"}
	conn = httplib.HTTPSConnection('open-sbox.sf-express.com')
	conn.request("POST",url,data,headers) 
	res =  conn.getresponse().read()
	conn.close()
	return json.loads(res)
def apply_access_token(appid='',appkey='',**kwargs):
	sf_req = {
		'head'				:	{
			'transType'		:	'301'					,
			'transMessageId':	kwargs['transMessageId'],
		},
		'body'				:	{}						,
	}
	url = '/public/v1.0/security/access_token/sf_appid/%s/sf_appkey/%s' % (appid,appkey)
	data = json.dumps(sf_req)
	return send_request(url,data)

def refresh_access_token(appid='',appkey='',**kwargs):
	sf_req = {
		'head'				:	{
			'transType'		:	'302'					,
			'transMessageId':	kwargs['transMessageId'],
		},
		'body'				:	{}						,
	}
	url = '/public/v1.0/security/refresh_token/access_token/%s/refresh_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],kwargs['refresh_token'],appid,appkey)
	data = json.dumps(sf_req)
	return send_request(url,data)

def query_access_token(appid='',appkey='',**kwargs):
	sf_req = {
		'head'				:	{
			'transType'		:	'300'					,
			'transMessageId':	kwargs['transMessageId'],
		},
		'body'				:	{}						,
	}
	url = '/public/v1.0/security/access_token/query/sf_appid/%s/sf_appkey/%s' % (appid,appkey)
	data = json.dumps(sf_req)
	return send_request(url,data)

def filter_order(appid='',appkey='',**kwargs):
	url = '/rest/v1.0/filter/access_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],appid,appkey)
	sf_req = {
		'head'					:	{
			'transType'			:	'204'																		,
			'transMessageId'	:	kwargs['transMessageId'		]												,
		},
		'body'					:	{
			'filterType'		:	kwargs['filterType'			] if 'filterType' 		in kwargs else '1'		,
			'consigneeAddress'	:	kwargs['consigneeAddress'	]												,
			'consigneeProvince'	:	kwargs['consigneeProvince'	]												,
			'consigneeCity'		:	kwargs['consigneeCity'		]												,
			'consigneeCounty'	:	kwargs['consigneeCounty'	]												,
			'consigneeCountry'	:	kwargs['consigneeCountry'	] if 'consigneeCountry' in kwargs else '中国'	,
		},
	}
	data = json.dumps(sf_req)
	return send_request(url,data)

def create_order(appid='',appkey='',**kwargs):
	url = '/rest/v1.0/order/access_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],appid,appkey)
	sf_req = {
		'head'						:	{
			'transType'				:	'200'																				,
			'transMessageId'		:	kwargs['transMessageId'			]													,
		},
		'body'						:	{
			'orderId'				:	kwargs['orderId'					]													,
			'expressType'			:	kwargs['expressType'				]													,
			'payMethod'				:	kwargs['payMethod'					]													,
			'custId'				:	kwargs['custId'						]													,
			#'isDocall'				:	kwargs['isDocall'					]	if 'isDocall'				in kwargs else '1'	,
			#'isGenBillno'			:	kwargs['isGenBillno'				] 	if 'isGenBillno' 			in kwargs else '1'	,
			#'isGenEletricPic'		:	kwargs['isGenEletricPic'			] 	if 'isGenEletricPic' 		in kwargs else '1'	,
			#'payArea'				:	kwargs['payArea'					] 	if 'payArea' 				in kwargs else ''	,
			#'sendStartTime'			:	kwargs['sendStartTime'				] 	if 'sendStartTime' 			in kwargs else ''	,
			#'needReturnTrackingNo'	:	kwargs['needReturnTrackingNo'		] 	if 'needReturnTrackingNo' 	in kwargs else ''	,
			#'remark'				:	kwargs['remark'						] 	if 'remark' 				in kwargs else ''	,
			#'deliverInfo'			:	{
			#	'company'			:	kwargs['deliverInfo']['company'		] 	if 'company' 				in kwargs else ''	,
			#	'contact'			:	kwargs['deliverInfo']['contact'		] 	if 'contact' 				in kwargs else ''	,
			#	'tel'				:	kwargs['deliverInfo']['tel'			] 	if 'tel' 					in kwargs else ''	,
			#	'province'			:	kwargs['deliverInfo']['province'	] 	if 'province' 				in kwargs else ''	,
			#	'city'				:	kwargs['deliverInfo']['city'		] 	if 'city' 					in kwargs else ''	,
			#	'county'			:	kwargs['deliverInfo']['county'		] 	if 'county' 				in kwargs else ''	,
			#	'address'			:	kwargs['deliverInfo']['address'		] 	if 'address' 				in kwargs else ''	,
			#	'shipperCode'		:	kwargs['deliverInfo']['shipperCode'	] 	if 'shipperCode'			in kwargs else ''	,
			#	'mobile'			:	kwargs['deliverInfo']['mobile'		] 	if 'mobile' 				in kwargs else ''	,
			#},
			'consigneeInfo'			:	{
				'company'			:	kwargs['consigneeInfo']['company'	]                									,
				'contact'			:	kwargs['consigneeInfo']['contact'	]                									,
				'tel'				:	kwargs['consigneeInfo']['tel'		]                    								, 
				'province'			:	kwargs['consigneeInfo']['province'	]                									,
				'city'				:	kwargs['consigneeInfo']['city'		]                 									, 
				'county'			:	kwargs['consigneeInfo']['county'	]                    								,
				'address'			:	kwargs['consigneeInfo']['address'	]                    								,
				#'shipperCode'		:	kwargs['consigneeInfo']['shipperCode']	if 'mobile'                 in kwargs else ''   ,
				#'mobile'			:	kwargs['consigneeInfo']['mobile'	]	if 'mobile'                 in kwargs else ''   ,
			},
			'cargoInfo'				:	{
				'cargo'				:	kwargs['cargoInfo']['cargo'			]													,
				#'parcelQuantity'	:	kwargs['cargoInfo']['parcelQuantity']	if 'parcelQuantity'			in kwargs else ''	,
				#'cargoCount'		:	kwargs['cargoInfo']['cargoCount'	]	if 'cargoCount'				in kwargs else ''	,
				#'cargoUnit'			:	kwargs['cargoInfo']['cargoUnit'		]	if 'cargoUnit'				in kwargs else ''	,
				#'cargoWeight'		:	kwargs['cargoInfo']['cargoWeight'	]	if 'cargoWeight'			in kwargs else ''	,
				#'cargoAmount'		:	kwargs['cargoInfo']['cargoAmount'	]	if 'cargoAmount'			in kwargs else ''	,
				#'cargoTotalWeight'	:	kwargs['cargoInfo']['cargoTotalWeight']	if 'cargoTotalWeight'		in kwargs else ''	,
			},
			#'addedServices'			:	{
			#	'COD'				:	kwargs['addedServices']['COD'   	]   if 'COD'       				in kwargs else ''   ,
			#	'CUSTID'			:	kwargs['addedServices']['CUSTID'   	]   if 'CUSTID'       			in kwargs else ''   ,
			#	'INSURE'			:	kwargs['addedServices']['INSURE'   	]   if 'INSURE'       			in kwargs else ''   ,
			#	'MSG'				:	kwargs['addedServices']['MSG'   	]   if 'MSG'       				in kwargs else ''   ,
			#	'PKFREE'			:	kwargs['addedServices']['PKFREE'   	]   if 'PKFREE'       			in kwargs else ''   ,
			#	'SINSURE'			:	kwargs['addedServices']['SINSURE'   ]   if 'SINSURE'       			in kwargs else ''   ,
			#	'SDELIVERY'			:	kwargs['addedServices']['SDELIVERY' ]   if 'SDELIVERY'       		in kwargs else ''   ,
			#	'SADDSERVICE'		:	kwargs['addedServices']['SADDSERVICE']  if 'SADDSERVICE' 		    in kwargs else ''   ,
			#},
		}
	}

	data = json.dumps(sf_req)
	return send_request(url,data)

def query_result(appid='',appkey='',**kwargs):
	url = '/rest/v1.0/order/query/access_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],appid,appkey)
	sf_req = {
		'head'				:	{
			'transType'		:	'203'					,
			'transMessageId':	kwargs['transMessageId'],
		},
		'body'				:	{
			'orderId'		:	kwargs['orderId'	   ],
		},
	}

	data = json.dumps(sf_req)
	return send_request(url,data)

def route_query(appid='',appkey='',**kwargs):
	url = '/rest/v1.0/route/query/access_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],appid,appkey)
	sf_req = {
		'head'				:	{
			'transType'		:	'501'														,
			'transMessageId':	kwargs['transMessageId'	]									,
		},
		'body'				:	{
			'trackingType'	:	kwargs['trackingType'	]									,
			'trackingNumber':	','.join(kwargs['trackingNumber'])							,
			'methodType'	:	kwargs['methodType'		] if 'methodType' in kwargs else '1',
		},
	}

	data = json.dumps(sf_req)
	return send_request(url,data)

def route_query_inc(appid='',appkey='',**kwargs):
	url = '/rest/v1.0/route/inc/query/access_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],appid,appkey)
	sf_req = {
		'head'				:	{
			'transType'		:	'504'					 ,
			'transMessageId':	kwargs['transMessageId'	],
		},
		'body'				:	{
			'orderId'		:	kwargs['orderId'		],
		},
	}

	data = json.dumps(sf_req)
	return send_request(url,data)

def access_order_img(appid='',appkey='',**kwargs):
	url = '/rest/v1.0/waybill/image/access_token/%s/sf_appid/%s/sf_appkey/%s' % (kwargs['access_token'],appid,appkey)
	sf_req = {
		'head'				:	{
			'transType'		:	'205'					 ,
			'transMessageId':	kwargs['transMessageId'	],
		},
		'body'				:	{
			'orderId'		:	kwargs['orderId'		],
		},
	}

	data = json.dumps(sf_req)
	return send_request(url,data)

if __name__ == '__main__':
	#pdb.set_trace()
	appid = '00014841'
	appkey = '58729CDBB45678286BC1F5A197905514'
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
	pdb.set_trace()
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

