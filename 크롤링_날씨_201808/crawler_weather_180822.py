#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 태원 - 타이니소어 배틀 정리 #180820

#알고리즘
'''
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy

url = 'http://m.kma.go.kr/m/index.jsp'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

weatherNowAll = []
weatherNow = []

#날씨 상황 전체 리스트 변환
rawWeather = bsObj.select('#w-item-wrapper > div > ul > li')
for idx, i in enumerate(rawWeather,0):
    weatherNowAll.append(i.text.strip())

#리스트 넘버링 출력
def numbering(p_num):
    for idx, i in enumerate(p_num,0):
        print(idx, i)


weatherNow = weatherNowAll[1:53]
weatherNowCopy = copy.copy(weatherNow)

#리스트의 공백 제거
def removeBlank(p_orignal,p_copy):
    for i in range(0,len(p_orignal)):
        if len(p_orignal[i]) == 0 or p_orignal[i] == '-':
            p_copy.remove(p_orignal[i])
        else:
            continue
    return p_copy
wNP = removeBlank(weatherNow,weatherNowCopy)

#오늘 날씨 출력
def weatherNow(p_copy):
    k = 0
    print('오늘의 날씨'.center(30,'='))
    for i in range(int(len(p_copy)/3)):
        print('%s \t\t %s \t %s' %(p_copy[k], p_copy[k+1], p_copy[k+2]))
        k += 3
    print()
    return
weatherNow(wNP)

#내일의 날씨
weatherNowAllCopy = copy.copy(weatherNowAll)
removeBlankWeatherAll = removeBlank(weatherNowAll,weatherNowAllCopy)
weatherTommorow = removeBlankWeatherAll[23:55]
numbering(weatherTommorow)
print(str(weatherTommorow[0]).center(40,'='))


#이시각 현재 날씨
rawWeatherToday = bsObj.select('#div_0 > div > div > p')
# for idx, i in enumerate(rawWeatherToday,0):
#     print(idx, i.text)