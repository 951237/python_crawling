#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pyautogui as pa


URL = 'http://www.teacher21.co.kr/'
URL_LECTURE = 'http://www.teacher21.co.kr/classroom/lecture_hojoon.asp'

# 사이트 접속하기
driver = webdriver.Chrome('chromedriver_win.exe')
print('사이트에 접속중..')
driver.get(URL)

# 수동로그인

# 강의실 이동
driver.get(URL_LECTURE)

# 학습하기 클릭
driver.find_element_by_xpath('//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[6]/td[3]/a').click()  # 학습하기 버튼은 tr[6]이 8, 10, 12 으로 2씩 늘어남.

# 강의창 선택하기
def findWindow():
    all = pa.getWindows()
    for i in all:
        if "That's Speaking" in i:
            r_window = i
            print('강의창 확인~')
        else:
            continue
    return r_window

def getPosition(p_win):
    pa.getWindow(p_win).set_foreground()
    result = pa.getWindow(p_win).get_position()
    print('윈도우 위치값 확인!')
    return result

def clickIwant(좌표):
    pa.click(leftX + 좌표[0],leftY + 좌표[1],clicks=1,interval=0.25)
    print(f'클릭 : {leftX + 좌표[0],leftY + 좌표[1]}')
    time.sleep(0.75)

def moveIwant(좌표):
    pa.moveTo(leftX + 좌표[0],leftY + 좌표[1])
    print(f'이동 : {leftX + 좌표[0],leftY + 좌표[1]}')
    time.sleep(0.75)

windws_lector = findWindow()
loc_windows_lector = getPosition(windws_lector)

leftX = loc_windows_lector[0]   # 강의 윈도우 왼쪽 위 x 좌표
leftY = loc_windows_lector[1]   # 강의 윈도우 왼쪽 위 y 좌표
print(leftX, leftY)
# 주행하기 이미지 캡쳐 (936, 307) 30*30 픽셀
coord_drive = (665, 138)
coord_letstudy = (368, 404)
coord_mp3 = (836, 350)
coord_saveas = (874, 453)

# 주행하기 클릭하기
clickIwant(coord_drive)
time.sleep(1)
clickIwant(coord_letstudy)

# 마우스 이동
moveIwant(coord_mp3)
# 마우스 우클릭
pa.click(button='right')

#클릭 - 다른 이름
clickIwant(coord_saveas)

# 키 입력 - 엔터

#






# 스크린샷 찍기

pa.screenshot('win_lector.png', region=loc_windows_lector)


# 주행 클릭하기


for i in range(1, 61):
    print(f'//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[{6 + (i*2)}]/td[3]/a')