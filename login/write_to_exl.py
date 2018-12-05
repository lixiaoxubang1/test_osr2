# -*- coding: utf-8 -*-

import xlrd
import xlwt
from xlutils.copy import copy
import os.path
import types
import requests
import json
import os
import time
import datetime
import unittest
import traceback
import delect_docx
import Download_cloadResume
import search_resume
import string
import resume_detail

# 打印运行的时间
locatimes = time.strftime('%Y.%m.%d.%H:%M:%S',time.localtime(time.time()))

# , formatting_info=True
rb = xlrd.open_workbook('test_excle.xls')
r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
sheet = wb.get_sheet(0)
# 返回下载方面的code码
sheet.write(0,1,"url")
sheet.write(0,2,"code")
sheet.write(0,0,locatimes)
sheet.write(1,1,"url_cloud_buy")
sheet.write(2,1,"url_resume")
sheet.write(3,1,"url_third_resume")
sheet.write(4,1,"url_candidate")
       #返回一个元祖
response_code_download = Download_cloadResume.download_clundResume()
sheet.write(1,2,response_code_download[0])
sheet.write(2,2,response_code_download[1])
sheet.write(3,2,response_code_download[2])
sheet.write(4,2,response_code_download[3])

# 返回倍搜、简历管理页面搜索code码与数据
sheet.write(6,0,"search")
sheet.write(6,1,"cloud_search_resume")
sheet.write(6,2,"private_search_resume")
sheet.write(8,0,"search_result")
response_code_private_search = search_resume.search_private_resume()
response_code_cloud_search = search_resume.search_resume_cloud()
    # 获取的值是list，但是写入到exl中必须是str类型的，所以要转类型
    # list与string之间转换类型
    # 直接转换没有效果，就借助一个for循环进行转换
a = response_code_cloud_search[1]
var = '.'.join(str(s) for s in a if s not in ['NONE','NULL'])

sheet.write(7,1,response_code_cloud_search[0])
sheet.write(8,1,var)
sheet.write(7,2,response_code_private_search[0])
sheet.write(8,2,response_code_private_search[1])


# 返回详情页面的code码和数据


wb.save('test_excle.xls')



