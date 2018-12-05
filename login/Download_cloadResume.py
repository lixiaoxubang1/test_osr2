# -*- coding: utf-8 -*-


import types
import requests
import json
import os
import time
import datetime
import unittest
import traceback
import delect_docx



# 拉勾的简历下载链接，在倍搜页面
url_cloud_buy = "https://www.belloai.com/api/cloud_resume/5bd2faca8defe20001ea4886/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJlNDQ1ZGFlMDgzN2MwMDAxNDg5YzcyIiwibW9iaWxlIjoiMTg2MDMwNjQ0MjgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.r7yMDZpcSwegxIMw87fQuZ335uQWfqtzEc8QeZJpYkE"
# 自己的简历下载，倍搜简历收藏到自己的简历管理页面，下载链接.
url_resume = "https://www.belloai.com/api/resume/5bee7239066d300001110921/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38"
# 云端简历购买或者没有购买，在倍搜页面的下载链接
url_third_resume = "https://www.belloai.com/api/third_party_resume/5bf28b00088326000147551d/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJkMzQ3NWJkM2ZmMTEwMDAxMDlmYTM1IiwibW9iaWxlIjoiMTg2MTcxMTA0OTgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.WXj2Cm6-_8oStuCJcTbzaOfnf-LU5P2yHFA8PF3yD38"
# 智能推荐处的简历下载
url_candidate = "https://www.belloai.com/api/candidate/5bf2a0fc6bda5c0001031731/export?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJlNDQ1ZGFlMDgzN2MwMDAxNDg5YzcyIiwibW9iaWxlIjoiMTg2MDMwNjQ0MjgiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.r7yMDZpcSwegxIMw87fQuZ335uQWfqtzEc8QeZJpYkE"


# 【下载简历】
def download_clundResume():

    response_url_cloud_buy = requests.get(url_cloud_buy)
    response_url_resume = requests.get(url_resume)
    response_url_third_resume = requests.get(url_third_resume)
    response_url_candidate = requests.get(url_candidate)

    # 打印文件内容
    # print (response_url_cloud_buy.text)
    # print ("--------------------------------------------------------------------------------------------------------------------------")
    # print (response_url_resume.text)
    # print ("--------------------------------------------------------------------------------------------------------------------------")
    # print (response_url_third_resume.text)
    # print ("--------------------------------------------------------------------------------------------------------------------------")
    # print (response_url_candidate.text)
    # print ("--------------------------------------------------------------------------------------------------------------------------")

    # 文件输出的code码
    response_url_cloud_buy_status_code = response_url_cloud_buy.status_code
    response_url_resume_status_code = response_url_resume.status_code
    response_url_third_resume_status_code = response_url_third_resume.status_code
    response_url_candidate_status_code = response_url_candidate.status_code

    print (response_url_cloud_buy.status_code)
    print (response_url_resume.status_code)
    print (response_url_third_resume.status_code)
    print (response_url_candidate.status_code)
    print ("--------------------------------------------------------------------------------------------------------------------------")


    # print (type(response_url_third_resume))
    # print (type(response_url_resume))
    # print (type(response_url_cloud_buy))
    # print (type(response_url_candidate))

    try:
        r = requests.get(url=url_cloud_buy)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        with open("cloud_buy.docx", "wb") as outfile:
            outfile.write(r.content)
            print("cloud_buy_pass")
    except Exception as e:
        print("cloud_buy_fail")

    try:
        r = requests.get(url=url_resume)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        with open("url_resume.docx", "wb") as outfile:
            outfile.write(r.content)
            print("url_resume_pass")
    except Exception as e:
        print("url_resume_fail")

    try:
        r = requests.get(url=url_third_resume)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        with open("url_third_resume.docx", "wb") as outfile:
            outfile.write(r.content)
            print("url_third_resume_pass")
    except Exception as e:
        print("url_third_resume_fail")

    try:
        r = requests.get(url=url_candidate)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        with open("url_candidate.docx", "wb") as outfile:
            outfile.write(r.content)
            print("url_third_resume_pass")
    except Exception as e:
        print("url_third_resume_fail")

    return response_url_cloud_buy_status_code, response_url_resume_status_code,response_url_third_resume_status_code,response_url_candidate_status_code

if __name__ == '__main__':
    download_clundResume()
