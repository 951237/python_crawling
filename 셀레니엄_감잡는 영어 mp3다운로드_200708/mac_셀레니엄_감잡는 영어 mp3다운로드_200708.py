#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui as pa

pa.FAILSAFE = True

URL = 'http://www.teacher21.co.kr/'
URL_LECTURE = 'http://www.teacher21.co.kr/classroom/lecture_hojoon.asp'

# 사이트 접속하기
driver = webdriver.Chrome('/Users/mac/Documents/coding_python/python_crawling/chromedriver_mac')
print('사이트에 접속중..')
driver.get(URL)

driver.get(URL_LECTURE)

driver.find_element_by_xpath()

# xpath 출력 해보기
for i in range(29, 61):
    v_xpath = f'//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[{i*2 + 6}]/td[3]'
    driver.find_element_by_xpath(v_xpath).click()
    time.sleep(3)

    # 주행하기 클
    # 주행하기 = pa.screenshot(region=(736, 177, 30, 30) ) # 강의실 입장하기 좌표
    img_주행하기 = pa.locateCenterOnScreen('drive.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)

    pa.click(img_주행하기) # 강의실 입장 센터값 클릭
    pa.click(img_주행하기) # 강의실 입장 센터값 클릭
    time.sleep(1)

    # 렛쯔 스터디 클릭릭
    img_스터디 = pa.locateCenterOnScreen('study.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)

    pa.click(img_스터디) # 강의실 입장 센터값 클릭
    pa.click(img_스터디) # 강의실 입장 센터값 클릭
    time.sleep(1)

    # 파일 우측클릭

    loc_mp3 = pa.locateCenterOnScreen('mp3.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)

    pa.moveTo(loc_mp3)
    pa.mouseDown(button='right')

    # 파일 저장하
    loc_save = pa.locateCenterOnScreen('save.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)
    pa.click(loc_save) # 강의실 입장 센터값 클릭
    time.sleep(2)

    loc_save_final = pa.locateCenterOnScreen('save_final.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)
    pa.moveTo(loc_save_final) # 강의실 입장 센터값 클릭
    pa.click(loc_save_final) # 강의실 입장 센터값 클릭
    time.sleep(1)

    #파일창 닫기
    # loc_save = pa.locateCenterOnScreen('close.png')  # 이미지파일 센터값 저장
    # time.sleep(0.25)
    # pa.moveTo(loc_save) # 강의실 입장 센터값 클릭
    # pa.click(loc_save) # 강의실 입장 센터값 클릭
    pa.hotkey('command', 'w')
    time.sleep(1)

# 6부터 2씩 증가하여 126까
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[6]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[8]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[62]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[64]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[126]/td[3]



pa.position()







# ------------------- 테스트 ----------------------------

pa.position()   #마우스 좌표 알아내기
enter = pa.screenshot(region=(572, 430, 30, 30) ) # 강의실 입장하기 좌표

#todo 스크린샷은 왜 전체화면만 저장될까? 개별파일로 저장은 안되나?

img_enter = pa.locateCenterOnScreen(enter)  # 이미지파일 센터값 저장
time.sleep(0.25)

pa.click(img_enter) # 강의실 입장 센터값 클릭

#todo 마우스는 이동하지만, 클릭이 되지 않음.
