import os
from io import BytesIO
from time import sleep
from urllib.request import urlretrieve as download

import pandas
from PIL import Image
from openpyxl import Workbook
from selenium import webdriver
from selenium.common.exceptions import *

DOWNLOAD_DIR = '/Users/mac/Documents/python_work/my_project/crawling/크롤링_' \
               '나라장터_200202/imgs '
# driver = webdriver.Chrome('/Users/mac/Documents/python_work/my_project'
#                          '/crawling/chromedriver_mac')
driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\python_crawling\chromedriver_win.exe')
driver.get('http://shopping.g2b.go.kr')  # 나라장터 사이트로 이동
driver.switch_to.frame('sub')  # 메인프레임속의 서브프레임으로 바꾸기

driver.find_element_by_css_selector("input#kwd.srch_txt").send_keys("작업용 의자")
# 검색어 '작업용 의자'입력
driver.find_element_by_css_selector("input#kwd.srch_txt").submit()  # 검색하기

필수옵션 = ['메시', '망사']
제외옵션 = '가죽'
driver.execute_script("javascript:attrNmValLink('5611210201', '등판재질',  "
                      "'ATTR_269556' , '' ); ")  # 자바스크립트 코드 실행

체크박스리스트 = driver.find_elements_by_css_selector(
    'ul#dLstDiv>li>input[type="checkbox"]')  # 체크박스의
# 텍스트가 인풋 태그 밖에 위치하여 체크박스를 모두 찾음.

for 체크박스 in 체크박스리스트: # 왜 안될까?
    parent = 체크박스.find_element_by_xpath('./..')  # 체크박스 상위를 부모로 변수를 만듦
    for i in 필수옵션:  # 필수옵션 리스트 2개 확인
        if i in parent.text and '가죽' not in parent:  # '메시'나 '망사'를 포함하지만,
            # '가죽'을 포함하지 않는다면
            체크박스.click()
