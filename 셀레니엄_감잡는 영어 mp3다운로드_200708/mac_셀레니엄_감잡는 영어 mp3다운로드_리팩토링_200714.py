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

# 함수 만들기
# 이미지 검색하여 이동하고 클릭하기
def img_search_move_click(p_img_file, p_click=None):
	loc_img = pa.locateCenterOnScreen(p_img_file)  # 이미지파일 센터값 저장
	time.sleep(0.25)

	pa.moveTo(loc_img)  # 강의실 입장 센터값 이동

	if p_click == 'right':
		pass
		pa.mouseDown(button='right')
	else:
		pa.click(loc_img)  # 강의실 입장 센터값 클릭

	time.sleep(1)  # 화면 바뀌기 대기


# xpath 출력 해보기
for i in range(50, 61):
	v_xpath = f'//*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[{i * 2 + 6}]/td[3]'  # 수업영상 팝업 xpath
	driver.find_element_by_xpath(v_xpath).click()
	time.sleep(3)

	# 주행하기 = pa.screenshot(region=(736, 177, 30, 30) ) # 강의실-주행하기 좌표 30*30으로 캡처하기
	img_search_move_click('drive.png')

	# 렛쯔 스터디 클릭
	img_search_move_click('study.png')

	# mp3 파일 다운로드 하기
	# 이미지 검색하기
	img_search_move_click('mp3.png', p_click='right')

	# 다른이름으로 파일 저장하기
	img_search_move_click('save.png')
	time.sleep(1)

	# 파일저장하기 창에서 저장하기 버튼 클릭하기
	img_search_move_click('save_final.png')

	# 파일창 닫기
	pa.hotkey('command', 'w')  # 파일창 닫기
	time.sleep(1)

# //*[@id="Table_02"]/tbody/tr[1]/td[2]/table[2]/tbody/tr[104]/td[3]