#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui as pa

pa.FAILSAFE = True

URL = 'http://www.teacher21.co.kr/'
URL_LECTURE = 'http://www.teacher21.co.kr/classroom/lecture_hojoon.asp'
PATH_DRIVER = 'C:\\Users\\User\\Documents\\coding_python\\crawling\\chromedriver_win.exe'
# 사이트 접속하기
driver = webdriver.Chrome(PATH_DRIVER)
print('사이트에 접속중..')
driver.get(URL)