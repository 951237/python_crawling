#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui as pa

URL = 'http://www.teacher21.co.kr/'
PATH_DRIVER = 'C:\\Users\\User\\Documents\\coding_python\\python_crawl\\chromedriver_win.exe'

# 사이트 접속하기
driver = webdriver.Chrome(PATH_DRIVER)
print('사이트에 접속중..')
driver.get(URL)

pa.position()

# 이미지캡처 - 나의 강의실
pa.screenshot('enter_in.png', region=(847, 681, 30, 30))

loc_enter = pa.locateCenterOnScreen('enter.png')

pa.click(loc_enter)
pa.click(loc_enter)

# 강의실 입장 이미지 검색
loc_enter_in = pa.locateCenterOnScreen('enter_in.png')

pa.click(loc_enter_in)
pa.click(loc_enter_in)







# 학습하기 클릭
driver.find_element_by_xpath('//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[6]/td[3]/a').click()  # 학습하기 버튼은 tr[6]이 8, 10, 12 으로 2씩 늘어남.



# 주행 클릭하기


for i in range(1, 61):
    print(f'//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[{6 + (i*2)}]/td[3]/a')