#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# 알고리즘
1. 로그인하기
2. 각 문제를 아이디값을 추출하기
    2-1. 아이디값을 조합하여 페이지로 이동하기
3. 각 문제에서 세부 문제의 아이디값 추출
    3-1. 세부문제의 아이디 값으로 페이지 이동하기
    3-2. 문제 수정하기

'''


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pyautogui as pa

url = 'https://www.plickers.com/login'

driver = webdriver.Chrome()
print('사이트에 접속중..')
driver.get(url)

def loginPlickers():
    # res = driver.execute_script("return document.documentElement.outerHTML")
    try:
        driver.forward()
        driver.maximize_window()
        time.sleep(0.25)

        print('구글계정으로 로그인 시도..')
        driver.find_element_by_xpath('//*[@id="App"]/div/div/div[2]/button').click()

        print('계정정보 입력중..')
        input('Press Enter... ')

    except Exception as e:
        print(e)

loginPlickers()

try:
    print('라이브러리로 이동중...')
    page = 'https://www.plickers.com/library'
    driver.get(page)
    res = driver.execute_script("return document.documentElement.outerHTML")

    print('페이지 파싱중...')
    bs_obj = BeautifulSoup(res, 'html.parser')
    allDiv = bs_obj.select('#focusableLibraryTable > div')

    print('문제 아이디값 추출...')
    for div in allDiv:
        for i in div.find_all(class_='cellRow'):
            print(i.get('id'))
except Exception as e:
    print(e)


# 셀레니움으로 문제로 이동하기
try:
    print('라이브러리로 이동중...')
    page = 'https://www.plickers.com/library'
    driver.implicitly_wait(3)
    driver.get(page)

    print('첫번째 목록으로 이동중...')
    driver.find_element_by_xpath('//*[@id="5aa52032ef8fb0000476a8dd"]/div/div[4]/button').click()

    time.sleep(0.25)
    #문제로 이동 //*[@id="5aa52087f9fd15000490275c"]/div/div[3]/button
    print('문제로 이동중...')
    driver.find_element_by_xpath('//*[@id="5aa52087f9fd15000490275c"]/div/div[3]/button').click()

    time.sleep(0.25)
    #편집 버튼 //*[@id="App"]/div[3]/div[2]/div[2]/div[4]/button[2]
    print('문제 수정중...')
    driver.find_element_by_xpath('//*[@id="App"]/div[3]/div[2]/div[2]/div[4]/button[2]').click()

    #이미지 템플릿 //*[@id="App"]/div[2]/div/div[2]/div/div[1]/div[1]/button[2]

    pa.hotkey('command','2')
    time.sleep(1)
    print('이미지 템플릿 적용중...')
    driver.find_element_by_xpath('//*[@id="App"]/div[2]/div/div[2]/div/div[1]/div[1]/button[2]').click()

    #탭 닫기
    pa.hotkey('command','w')

except Exception as e:
    print(e)

#focusableLibraryTable > div
#focusableLibraryTable > div