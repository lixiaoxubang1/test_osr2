# -*- coding: utf-8 -*-

import types
import requests
import json
import os
import time
import datetime
import unittest
import traceback

# 私有简历
private_resume_url = 'https://www.belloai.com/api/resume/search'
private_datas = {"category": "private", "city": "", "year_of_work_experience": "", "skills": [], "industries": [],
		"employments": [], "educations": [], "keyword": "hr", "gender": "", "page": 1, "max_results": 25}
private_headers = {"cache-control": "no-cache", "content-type": "application/json",
		   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJlNDQ1ZGFlMDgzN2MwMDAxNDg5YzcyIiwibW9iaWxlIjoiMTg2MDMwNjQ0MjgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.r7yMDZpcSwegxIMw87fQuZ335uQWfqtzEc8QeZJpYkE", }

# 倍搜简历
cloud_resume_url = 'https://www.belloai.com/api/resume/search'
cloud_datas = {"category": "cloud", "city": "", "skills": [], "industries": [], "employments": [], "educations": [],
		 "keyword": "ui", "gender": "男", "resume_update_time": {"days": 30, "gte": "2018-10-21T00:00:00"},
		 "page": 1, "max_results": 25}
cloud_headers = {"cache-control": "no-cache", "content-type": "application/json",
		   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38", }


# 搜索倍搜列表，返回倍搜列表中数据都是三个渠道的数据
def search_resume_cloud():

	response = requests.request("post", cloud_resume_url, headers = cloud_headers, data=json.dumps(cloud_datas))
	search_resume_cloud_response_code = response.status_code
	print("resume_cloud code is : " + str(search_resume_cloud_response_code))
	# print (response.text)
	msg = response.json()

	if 'items' in msg:
		# 打印response json 列表相同字段中的值
		# python循环获取json数组中某个值
		# https://segmentfault.com/q/1010000011227611
		# item是字典类型，get方法
		result = [(item.get('channel', 'NA'), item.get('external_id', 'NA')) for item in msg['items']]
		# 打印出来字典类型的结果
		print(result)
		print(type(result))
	# print(msg['items'])
	else:
		print('not exist')

	return search_resume_cloud_response_code,result
# 搜索私有简历，结果为1即为正确
def search_private_resume():

	response = requests.request("post",private_resume_url,headers = private_headers,data = json.dumps(private_datas))
	search_private_resume_response_code = response.status_code
	print ("private_resume code is : " + str(search_private_resume_response_code))
	msg = response.json()
	total = str(msg['meta']['total'])
	print ('search total is : ' + total + '个')
	return search_private_resume_response_code,total


if __name__ == '__main__':
	search_private_resume()
	search_resume_cloud()






# 查看简历详情
# url = "https://www.belloai.com/api/third_party_resume/jzd/223752708?included=[%22my_order%22,%22my_resume%22,%22resume_doubt%22,%22risks%22]"
# headers = {"cache-control": "no-cache","content-type": "application/json" , "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38",}
#
# response = requests.get(url,headers = headers)
# print (response.status_code)
# print (response.text)
