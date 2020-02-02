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
from selenium import webdriver
import time

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
    allDiv = bs_obj.select('#focusableLibraryTable')

    print('문제 아이디값 추출...')
    for div in allDiv:
        for i in div.find_all(class_='cellRow'):
            iID = i.get('id')  # 5, 6학년 차시별 아이디 추출하기
            subPage01 = 'https://www.plickers.com/library/%s' % (iID)  # 차시별 주소 구하기
            driver.get(subPage01)  # 차시별 사이트로 이동

            time.sleep(3)
            res = driver.execute_script("return document.documentElement.outerHTML")
            bs_objSub = BeautifulSoup(res, 'html.parser')
            allDivSub = bs_objSub.select('#focusableLibraryTable')

            for div in allDivSub:
                for i in div.find_all(class_='cellRow'):
                    subID = i.get('id')  # 차시내 문제 아이디 추출하기
                    #                     subPage02 = 'https://www.plickers.com/question/%s' % (subID)  # 문제 주소 구하기
                    #                     driver.get(subPage02)  # 문제로 이동

                    time.sleep(3)
                    print('문제 수정중...')
                    subPage03 = 'https://www.plickers.com/editor/%s' % (subID)  # 문제 편집 사이트 주소 구하기
                    driver.get(subPage03)  # 편집주소로 이동하기

                    time.sleep(3)
                    print('이미지 템플릿 적용중...')
                    driver.find_element_by_xpath('//*[@id="App"]/div[2]/div/div[2]/div/div[1]/div[1]/button[2]').click()
                    time.sleep(3)
        print('작업 완료')
        driver.get(page)
    print('작업완료...')

except Exception as e:
    print(e)
