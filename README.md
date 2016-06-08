# non official python sdk

#简介
因为顺丰官方未提供python的SDK，技术支持人员的回复也不够及时。因此在接入的时候花了一点时间。为了避免将来的人走同样的弯路，将自己的代码稍加整理开源出来供参考

#前提
httplib
json
datetime
sys

#安装
python setup.py install

#授权
仅限用于学习交流，请勿用于任何商业用途。

#使用
下边的使用都假设用户已经申请了顺丰开放平台的appid和appkey
返回的数据格式见顺丰官方文档
为保证包的独立性并不失代表性，transMessageId此处的生成方式不能保证多线程的情况下唯一，请用户自行设计
##申请access_token
apply_access_token(
	appid=appid,
	appkey=appkey,
	transMessageId=datetime.now().strftime('%y%m%d%H%M%S%f')
)
##查询access_token
query_access_token(
	appid=appid,
	appkey=appkey,
	transMessageId=datetime.now().strftime('%y%m%d%H%M%S%f')
)
##更新token
sf_req = { 
	'transMessageId'    :   datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'      :   access_token,
	'refresh_token'		:	refresh_token,
}
refresh_access_token(
	appid=appid,
	appkey=appkey,
	**sf_req
)
##订单筛选
sf_req = { 
	'transMessageId'    :   datetime.now().strftime('%y%m%d%H%M%S%f'),
	'access_token'      :   access_token,
	'filterType'        :   '1',
	'consigneeAddress'  :   '东方路985号',
	'consigneeProvince' :   '上海市',
	'consigneeCity'     :   '上海市',
	'consigneeCounty'   :   '浦东新区',
	'consigneeCountry'  :   '中国',
}   
filter_order(appid=appid,appkey=appkey,**sf_req)
##创建订单
sf_req = { 
    'transMessageId'    :   datetime.now().strftime('%y%m%d%H%M%S%f'),
    'access_token'      :   access_token,
    'refresh_token'     :   refresh_token,
    'orderId'           :   order_id,
    'expressType'       :   '1',
    'payMethod'         :   '1',
    'custId'            :   '7000010000',
    'consigneeInfo'     :   {   
        'company'       :   '个人',
        'contact'       :   '刘先生',
        'tel'           :   '15000000000',
        'province'      :   '北京市',
        'city'          :   '北京市',
        'county'        :   '海淀区',
        'address'       :   '学院路路10号',
    },  
    'cargoInfo'         :   {   
        'cargo'         :   '食品',
    },  
}   
create_res = create_order(appid=appid,appkey=appkey,**sf_req)
##订单结果查询
sf_req = {
    'transMessageId'    :   datetime.now().strftime('%y%m%d%H%M%S%f'),
    'access_token'      :   access_token,
	'orderId'			:	order_id,
}
	
query_result(
	appid=appid,
	appkey=appkey,
	**sf_req
)
##路由查询
sf_req = { 
    'transMessageId'    :   datetime.now().strftime('%y%m%d%H%M%S%f'),
    'access_token'      :   access_token,
    'trackingType'      :   '1',
    'trackingNumber'    :   [mail_no],#此处的mail_no在上一个接口得到的结果中
}   
route_query(
	appid=appid,
	appkey=appkey,
	**sf_req
)
##获取运单图片
sf_req = {
    'transMessageId'    :   datetime.now().strftime('%y%m%d%H%M%S%f'),
    'access_token'      :   access_token,
    'orderId'           :   order_id,
}
access_order_img(
	appid=appid,
	appkey=appkey,
	**sf_req
)
