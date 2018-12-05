# -*- coding: utf-8 -*-

'''
@author:coco
@version:
@see:
@time：2018/11/16
'''

import types
import requests
import json
import os
import time
import datetime
import unittest
import traceback
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
from selenium import webdriver
from email.mime.application import MIMEApplication

# 唤起浏览器，访问osr登录地址
driver = webdriver.Chrome()
base_url = 'https://belloai.com/osr/#/login'
driver.get(base_url)
time.sleep(20)

# 登录函数
def selenium_login():

    account = driver.find_element_by_name('loginForm_account')
    time.sleep(5)
    account.send_keys('18617110498')
    time.sleep(5)
    password = driver.find_element_by_name('loginForm_password')
    time.sleep(5)
    password.send_keys('123456')
    time.sleep(5)

    login_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[3]/button')
    login_button.click()
    time.sleep(20)

if __name__ == '__main__':
    selenium_login()
