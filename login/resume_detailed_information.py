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
import datetime
from selenium import webdriver
import login


def resume_detailed_information():
    # 调用login函数
    login.selenium_login()
    print("login success")
    time.sleep(10)
    print("witing visit detailed_information...")
    # 调用login函数中的dirver，但是dirver必须是共有字段，不能在函数内
    button = login.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]')
    button.click()
    print("detailed_information success!")
    time.sleep(20)
    print("witing next detailed_information...")
    button1 = login.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[4]/div/div/div[2]/div[1]/i')
    button1.click()
    print("second resume detailed_information success!")
    time.sleep(20)
    # 关闭详情页面弹窗
    print("close the window...")
    button2 = login.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[3]/div[2]/div[4]/div/div/div[2]/i')
    button2.click()
    print("close the window success!")
    time.sleep(3)

def cloud_resume_detailed_information():
    #resume_detailed_information()
    login.selenium_login()
    time.sleep(10)
    button = login.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/ul/li[2]/div/span/span')
    button.click()
    time.sleep(20)
    try:
        search_input = login.driver.find_element_by_id('search_input')
        search_input.send_keys('python')
    except StaleElementReferenceException as msg:
        print("error")
        search_input = login.driver.find_element_by_id('search_input')
        search_input.send_keys('python')
    time.sleep(10)
    search_button = login.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/button[1]')
    search_button.click()
    time.sleep(20)


if __name__ == '__main__':
    resume_detailed_information()
    #cloud_resume_detailed_information()