#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 라이브러리 임포트
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# 스택어버클로 로그인
URL = 'https://stackoverflow.com'


# 웹드라이버 구동
driver = webdriver.Chrome()
print('사이트 접속중...')
driver.get(URL)

# 유투브 로그인 - 스택어버플로 경유해야 셀레니움 로그인 가능함.

URL_TUBE_MUSIC = 'https://www.youtube.com/audiolibrary/music?nv=1'
URL_TUBE_EFFECT = 'https://www.youtube.com/audiolibrary/soundeffects?ar=1593957061024&nv=1'


# 무료 음악 다운로드

driver.get(URL_TUBE_MUSIC)
time.sleep(1)

# 페이지 소스 가져오기
res = driver.execute_script("return document.documentElement.outerHTML")
bs_obj = BeautifulSoup(res, 'html.parser')

content = bs_obj.find('div', {'class' : 'track-content'})
time.sleep(1)
print(len(content))

track_list = content.find('ul', {'class' : 'track-list'})
time.sleep(1)
print(len(track_list))

tracks = track_list.find_all('li', {'class' : 'track'})
time.sleep(1)
print(len(tracks))


# 무료음악 다운로드 반복
try:
    for i in range(1, 275):
        v_music_xpath = f'//*[@id="audio-library-content"]/div[5]/div[2]/ul/li[{i}]/div[1]/div[8]/a'
        driver.find_element_by_xpath().click()
        time.sleep(1)

except:
    print('더이상 없음.')


# 음향효과 다운로드
URL_TUBE_EFFECT = 'https://www.youtube.com/audiolibrary/soundeffects?ar=1593957061024&nv=1'
driver.get(URL_TUBE_EFFECT)
time.sleep(1)

# 페이지 소스 가져오기
res = driver.execute_script("return document.documentElement.outerHTML")
bs_obj = BeautifulSoup(res, 'html.parser')

content = bs_obj.find('div', {'class' : 'track-content'})
time.sleep(1)
print(len(content))

track_list = content.find('ul', {'class' : 'track-list'})
time.sleep(1)
print(len(track_list))

tracks = track_list.find_all('li', {'class' : 'track'})
time.sleep(1)
print(len(tracks))

try:
    for i in range(1051, 1714):
        v_effect_xpath = f'//*[@id="audio-library-content"]/div[4]/div[2]/ul/li[{i}]/div[1]/div[6]/a'
        driver.find_element_by_xpath(v_effect_xpath).click()
        time.sleep(1)

except:
    print('더이상 없음.')

