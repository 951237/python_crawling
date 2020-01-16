#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 다음 일기예보 #180822


from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy

url = 'https://m.search.daum.net/search?nil_profile=btn&w=tot&DA=SBC&q=%EC%83%88%EC%86%94%EB%8F%99+%EB%82%A0%EC%94%A8'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

rawListAll = []

#날씨 간추림 - 달력의 모양임. 최고,최저 기온을 보여줌.
rawSourceCal = bsObj.select('#slide-1 > div > div > table > thead > tr > td')

#날씨 상황 전체 리스트 변환
rawSourceList = []
rawSource = bsObj.select('#weatherNColl > div > div')
for _i in rawSource:
    liAll = _i.findAll('li')
    for idx, i in enumerate(liAll,0):
        rawSourceList.append(i.text.strip())

# for idx, i in enumerate(rawSourceList):
#     print(idx,i)

selTime = rawSourceList[0:3] #슬라이스 오늘, 내일, 모레
selWeather = rawSourceList[4:-3] #슬라이스 날씨, 바람, 습도 - 오늘, 내일, 모레

k = 0
fL = []

#날씨를 오늘, 내일, 모래로 나누어서 리스트로 저장
for f0 in range(3):
    fT01 = []
    for f1 in range(3):
        fT02 = []
        for f2 in range(8):
            a = selWeather[k].replace('\n',' ')
            fT02.append(a)
            k += 1
        fL.append(fT02)

#날씨 출력하기
'''
'오늘 08.22 0'의 날씨
0시 구름 000 / 0시 바람 010 / 0시 습도 020
3시 구름 001/ 3시 바람 011/ 3시 습도 021
...
21시 구름 007 / 21시 바람 017 / 21시 습도 027

'내일 '의 날씨

'''
k = 0
for i in range(3): #오늘, 내일, 모래 3번 반복
    print(' 화성시 새솔동 %s의 날씨 '.center(50,'=') %(selTime[i]))
    for f1 in range(8): #fL리스트의 값이 9개임
        a = fL[k][f1]
        b = fL[k+1][f1]
        c = fL[k+2][f1]
        print('%s / %s / %s' %(a, b, c))
    k += 3
    print()


# for f0 in range(3):
#     fT = []
#     for f1 in range(8):
#         ff = str(f0)+str(f1)
#         fT.append(ff)
#     fL.append(fT)
# print(fL)
