#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'http://bms.ken.go.kr'

# 함수 - bs4로 html 가져오기
driver = webdriver.Chrome()
print('사이트에 접속중..')
driver.get(url)

try:
    driver.forward()
    driver.maximize_window()
    time.sleep(0.25)
    print('아이디 입력중...')
    driver.find_element_by_xpath('//*[@id="SSO_USER_ID"]').send_keys('driver1')

    time.sleep(1)
    input('Press Enter to continue...')

    print('인증서 선택...')
    driver.find_element_by_xpath('//*[@id="kc_cert_position"]/tbody/tr[2]/td[2]/button').click()

    time.sleep(0.25)
    driver.find_element_by_xpath('//*[@id="kc_cert_position"]/tbody/tr[2]/td[2]/ul/li[1]/a').click()

    print('비밀번호를 입력하세요...')
    time.sleep(0.25)
    driver.find_element_by_xpath('//*[@id="kc_content_default"]/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr/td[2]/form/input').click()
    input('Press Enter to continue...')

except Exception as e:
    print(e)


# driver.find_element_by_xpath('//*[@id="aQcnt_A01"]/img').click()
# input('Press Enter to continue...')
#
# driver.get('http://bms.ken.go.kr/cz/cb/viw/retrieveSanctnWaitDocList.do')
# res = driver.execute_script("return document.documentElement.outerHTML")
# bs_obj = BeautifulSoup(res, 'html.parser')
# print(bs_obj)
#
# print('결재목록 가져오기')
# list_tr = bs_obj.select('//*[@id="tbList"]/tbody')
#
# for i in list_tr:
#     print(i.text)








