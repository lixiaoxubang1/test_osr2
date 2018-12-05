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

cloud_url = "https://www.belloai.com/api/third_party_resume/szyc/1034134252"
cloud_datas = "included=[%22my_order%22,%22my_resume%22,%22resume_doubt%22,%22risks%22]"
# 18617004102 该账号的tokon
cloud_headers = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJjMGFlNmNjOTRjZjYwMDAxZjljNTdiIiwibW9iaWxlIjoiMTg2MTcwMDQxMDIiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.mfoEkZmyzhbIVzYWCjYngqikFd_DExr1C_Z2XenD7VQ"}

private_datas = "included=[%22my_order%22,%22risks%22]"
private_url = "https://www.belloai.com/api/resume/5bdc0f0c274c7700016fc77c"
private_headers = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNWJjMGFlNmNjOTRjZjYwMDAxZjljNTdiIiwibW9iaWxlIjoiMTg2MTcwMDQxMDIiLCJlbWFpbCI6bnVsbCwicm9sZSI6ImhyIiwidXNlcl90eXBlIjoxLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsInB1cmNoYXNlIiwidmlld19vcmRlciIsInZpZXdfcmVwb3J0Iiwidmlld19yZXN1bWUiXSwiaXNfYXV0aF9jbG91ZF9yZXN1bWUiOnRydWV9.mfoEkZmyzhbIVzYWCjYngqikFd_DExr1C_Z2XenD7VQ"}



def cloud_resume_detail():
    response = requests.request("get", cloud_url, headers=cloud_headers, data=cloud_datas)
    search_resume_cloud_response_code = response.status_code
    print("cloud_resume_detail code is : " + str(search_resume_cloud_response_code))
    msg = response.json()
    print(msg)

def private_resume_detail():
    response = requests.request("get", private_url, headers=private_headers, data=private_datas)
    search_resume_private_response_code = response.status_code
    print("private_resume_detail code is : " + str(search_resume_private_response_code))
    msg = response.json()
    print(msg)

if __name__ == '__main__':
    cloud_resume_detail()
    private_resume_detail()