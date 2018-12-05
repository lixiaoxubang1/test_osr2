# -*- coding: utf-8 -*-

import types
import requests
import json
import os
import time
import datetime
import unittest
import traceback
import smtplib
import datetime
from selenium import webdriver
import HTMLTestRunner
import sys

# 云端简历详情
cloud_url = "https://www.belloai.com/api/third_party_resume/szyc/1034134252"
cloud_detail_datas = "included=[%22my_order%22,%22my_resume%22,%22resume_doubt%22,%22risks%22]"
# 18617004102 该账号的tokon
cloud_detail_headers = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJjMGFlNmNjOTRjZjYwMDAxZjljNTdiIiwibW9iaWxlIjoiMTg2MTcwMDQxMDIiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.mfoEkZmyzhbIVzYWCjYngqikFd_DExr1C_Z2XenD7VQ"}
# 个人简历详情
private_detail_datas = "included=[%22my_order%22,%22risks%22]"
private_url = "https://www.belloai.com/api/resume/5bdc0f0c274c7700016fc77c"
private_detail_headers = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJjMGFlNmNjOTRjZjYwMDAxZjljNTdiIiwibW9iaWxlIjoiMTg2MTcwMDQxMDIiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.mfoEkZmyzhbIVzYWCjYngqikFd_DExr1C_Z2XenD7VQ"}


# 拉勾的简历下载链接，在倍搜页面
url_cloud_buy = "https://www.belloai.com/api/cloud_resume/5bd2faca8defe20001ea4886/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJlNDQ1ZGFlMDgzN2MwMDAxNDg5YzcyIiwibW9iaWxlIjoiMTg2MDMwNjQ0MjgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.r7yMDZpcSwegxIMw87fQuZ335uQWfqtzEc8QeZJpYkE"
# 自己的简历下载，倍搜简历收藏到自己的简历管理页面，下载链接.
url_resume = "https://www.belloai.com/api/resume/5bee7239066d300001110921/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38"
# 云端简历购买或者没有购买，在倍搜页面的下载链接
url_third_resume = "https://www.belloai.com/api/third_party_resume/5bf28b00088326000147551d/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38"
# 智能推荐处的简历下载
url_candidate = "https://www.belloai.com/api/candidate/5bf2a0fc6bda5c0001031731/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJlNDQ1ZGFlMDgzN2MwMDAxNDg5YzcyIiwibW9iaWxlIjoiMTg2MDMwNjQ0MjgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.r7yMDZpcSwegxIMw87fQuZ335uQWfqtzEc8QeZJpYkE"


# 私有简历
private_resume_url = 'https://www.belloai.com/api/resume/search'
private_resume_datas = {"category": "private", "city": "", "year_of_work_experience": "", "skills": [], "industries": [],
		"employments": [], "educations": [], "keyword": "hr", "gender": "", "page": 1, "max_results": 25}
private_resume_headers = {"cache-control": "no-cache", "content-type": "application/json",
		   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJlNDQ1ZGFlMDgzN2MwMDAxNDg5YzcyIiwibW9iaWxlIjoiMTg2MDMwNjQ0MjgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.r7yMDZpcSwegxIMw87fQuZ335uQWfqtzEc8QeZJpYkE", }

# 倍搜简历
cloud_resume_url = 'https://www.belloai.com/api/resume/search'
cloud_resume_datas = {"category": "cloud", "city": "", "skills": [], "industries": [], "employments": [], "educations": [],
		 "keyword": "ui", "gender": "男", "resume_update_time": {"days": 30, "gte": "2018-10-21T00:00:00"},
		 "page": 1, "max_results": 25}
cloud_resume_headers = {"cache-control": "no-cache", "content-type": "application/json",
		   "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38", }

class search(unittest.TestCase):

    def setUp(self):
        pass   # 在初始化方法中实例化一个对象，这样就不需要在每个用例中再进行实例化了

    # 搜索倍搜列表，返回倍搜列表中数据都是三个渠道的数据
    def search_resume_cloud(self):
        response = requests.request("post", cloud_resume_url, headers=cloud_resume_headers, data=json.dumps(cloud_resume_datas))
        search_resume_cloud_response_code = response.status_code
        self.assertEqual(search_resume_cloud_response_code, 200, 'fail')
        msg = response.json()
        if 'items' in msg:
            # 打印response json 列表相同字段中的值
            # python循环获取json数组中某个值
            # https://segmentfault.com/q/1010000011227611
            # item是字典类型，get方法
            result = [(item.get('channel', 'NA'), item.get('external_id', 'NA')) for item in msg['items']]
            # 打印出来字典类型的结果
            print(result)
        return

    # 搜索私有简历，结果为1即为正确
    def search_private_resume(self):

        response = requests.request("post", private_resume_url, headers=private_resume_headers, data=json.dumps(private_resume_datas))
        search_private_resume_response_code = response.status_code
        msg = response.json()

        self.assertEqual(search_private_resume_response_code, 200, 'fail')
        total = str(msg['meta']['total'])
        print('search total is : ' + total + '个')
        return total

class Test_resume_detail(unittest.TestCase):

    def setUp(self):
        pass   # 在初始化方法中实例化一个对象，这样就不需要在每个用例中再进行实例化了

    def cloud_resume_detail(self):
        response = requests.request("get", cloud_url, headers=cloud_detail_headers, data=cloud_detail_datas)
        search_resume_cloud_response_code = response.status_code
        self.assertEqual(search_resume_cloud_response_code, 200, 'fail')
        msg = response.json()
        print(msg)
        return

    def private_resume_detail(self):
        response = requests.request("get", private_url, headers=private_detail_headers, data=private_detail_datas)
        search_resume_private_response_code = response.status_code
        self.assertEqual(search_resume_private_response_code, 200, 'fail')
        msg1 = response.json()
        print(msg1)
        return

class download_Resume(unittest.TestCase):
    def setUp(self):
        pass

    def download_cloud_buy(self):
        response_url_cloud_buy = requests.get(url_cloud_buy)
        # 文件输出的code码
        response_url_cloud_buy_status_code = response_url_cloud_buy.status_code
        self.assertEqual(response_url_cloud_buy_status_code, 200, 'fail')

    def download_resume(self):
        response_url_resume = requests.get(url_resume)
        response_url_resume_status_code = response_url_resume.status_code
        self.assertEqual(response_url_resume_status_code, 200, 'fail')

    def download_third_resume(self):
        response_url_third_resume = requests.get(url_third_resume)
        response_url_third_resume_status_code = response_url_third_resume.status_code
        self.assertEqual(response_url_third_resume_status_code, 200, 'fail')

    def download_candidate(self):
        response_url_candidate = requests.get(url_candidate)
        response_url_candidate_status_code = response_url_candidate.status_code
        self.assertEqual(response_url_candidate_status_code, 200, 'fail')


if __name__ == '__main__':

    result = unittest.TextTestResult(sys.stdout,'test result',1)
    testcase = Test_resume_detail('cloud_resume_detail')
    testcase3 = Test_resume_detail('private_resume_detail')
    testcase.run(result)
    testcase3.run(result)
    testcase1 = search('search_resume_cloud')
    testcase2 = search('search_private_resume')
    testcase1.run(result)
    testcase2.run(result)

    suite = unittest.TestSuite()  # 定义一个测试套件
    filePath = '/Users/david/Documents/report/testresult.html'  # 确定生成报告的路径
    fp = open(filePath,'wb')
    suite.addTest(Test_resume_detail('cloud_resume_detail'))    #添加测试用例方法一：往测试套件里新增一条测试用例，测试用例只能用一种方法，同时两种会报错
    suite.addTest(Test_resume_detail('private_resume_detail'))
    suite.addTest(download_Resume('download_cloud_buy'))
    suite.addTest(download_Resume('download_resume'))
    suite.addTest(download_Resume('download_third_resume'))
    suite.addTest(download_Resume('download_candidate'))
    suite.addTest(search('search_resume_cloud'))
    suite.addTest(search('search_private_resume'))
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description='详细测试用例结果',    #不传默认为空
        )

    runner.run(suite)  # 运行，注意上述方法我写一起了，运行的话只能运行一种，另一个要注释
    fp.close()
