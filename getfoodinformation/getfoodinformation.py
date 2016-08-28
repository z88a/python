#coding:utf-8
#python 2.7
#author zhang88a

import urllib2,urllib,json,sys

def getshipin(foodcode):
	#reload(sys)   
	#sys.setdefaultencoding('utf8')
	url = 'http://www.foods12331.cn/food/detail/getFoodBrandByBarCode.json'
	values = {
	'bar_code':foodcode}
	data = urllib.urlencode(values)
	req = urllib2.urlopen(url,data)
	food = req.read().decode('utf-8')
	#print food
	
	food = json.loads(food)
	msg = food["resultData"]
	#print msg
	if msg==None:
		ans=u"条码："+foodcode+u"\n没有该食品的信息"
	else:
		brandname = food["resultData"]["brandName"]
		productName = food["resultData"]["productName"]
		partyContactName = food["resultData"]["partyContactName"]
		ans=u"条码："+foodcode+u"\n食品名称："+productName+u"\n生产企业："+partyContactName
	
	'''
	url = 'http://www.foods12331.cn/food/detail/findFoodByPage.json'
	values = {filters:{
	"food_type":"",
	"check_flag":"合格",
	"order_by":"1",
	"pageNo":0,
	"pageSize":20,
	"bar_code":foodcode,
	"sampling_province":"",
	"name_first_letter":None,
	"food_name":brandname}}
	data = urllib.urlencode(values)
	req = urllib2.urlopen(url,data)
	hege = req.read().decode('utf-8')
	print hege
	hege =json.loads(hege)
	'''
	
	 
	return ans
	

	
if __name__=='__main__':
	foodcode ='6944839996506'
	aa=getshipin(foodcode)
	print aa