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

# 수동 - 강의실까지 입장핳기

# xpath 출력 해보기
for i in range(29, 61):
    v_xpath = f'//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[{i*2 + 6}]/td[3]'   # 수업영상 팝업 xpath
    driver.find_element_by_xpath(v_xpath).click()
    time.sleep(3)

    # 주행하기 = pa.screenshot(region=(736, 177, 30, 30) ) # 강의실-주행하기 좌표 30*30으로 캡처하기
    img_주행하기 = pa.locateCenterOnScreen('drive.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)

    pa.moveTo(img_주행하기) # 강의실 입장 센터값 이동
    pa.click(img_주행하기) # 강의실 입장 센터값 클릭
    time.sleep(1)   # 화면 바뀌기 대기

    # 렛쯔 스터디 클릭
    img_스터디 = pa.locateCenterOnScreen('study.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)

    pa.moveTo(img_스터디) # 렛쯔 스터디 센터값 이동
    pa.click(img_스터디) # 렛쯔 스터디 센터값 클릭
    time.sleep(1)

    # mp3 파일 다운로드 하기
    # 이미지 검색하기
    loc_mp3 = pa.locateCenterOnScreen('mp3.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)

    # 파일 우측클릭
    pa.moveTo(loc_mp3)  # 이미지 센터값으로 이동
    pa.mouseDown(button='right')    # 위치값에서 우클릭하기

    # 다른이름으로 파일 저장하기
    loc_save = pa.locateCenterOnScreen('save.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)
    pa.click(loc_save) # 이미지 센터값 클릭
    time.sleep(2)

    # 파일저장하기 창에서 저장하기 버튼 클릭하기
    loc_save_final = pa.locateCenterOnScreen('save_final.png')  # 이미지파일 센터값 저장
    time.sleep(0.25)
    pa.moveTo(loc_save_final) # 저장하기 버튼으로 이동
    pa.click(loc_save_final) # 저장하기 버튼 클릭
    time.sleep(1)

    # 파일창 닫기
    pa.hotkey('command', 'w') # 파일창 닫기
    time.sleep(1)

# 6부터 2씩 증가하여 126까지
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[6]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[8]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[62]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[64]/td[3]
# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[126]/td[3]


# pa.position()     마우스 위치값 찾기

