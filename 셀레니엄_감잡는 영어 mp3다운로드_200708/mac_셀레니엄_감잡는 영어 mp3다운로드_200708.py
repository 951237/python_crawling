#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui as pa


URL = 'http://www.teacher21.co.kr/'
URL_LECTURE = 'http://www.teacher21.co.kr/classroom/lecture_hojoon.asp'

# 사이트 접속하기
driver = webdriver.Chrome('/Users/mac/Documents/coding_python/python_crawling/chromedriver_mac')
print('사이트에 접속중..')
driver.get(URL)


pa.position()   #마우스 좌표 알아내기
enter = pa.screenshot(region=(572, 430, 30, 30) ) # 강의실 입장하기 좌표

#todo 스크린샷은 왜 전체화면만 저장될까? 개별파일로 저장은 안되나?

img_enter = pa.locateCenterOnScreen(enter)  # 이미지파일 센터값 저장
time.sleep(0.25)

pa.click(img_enter) # 강의실 입장 센터값 클릭

#todo 마우스는 이동하지만, 클릭이 되지 않음.
