#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 태원 - 타이니소어 배틀 정리 #180820

#알고리즘
'''
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://namu.wiki/w/%EA%B3%B5%EB%A3%A1%EB%A9%94%EC%B9%B4%EB%93%9C/%EB%93%B1%EC%9E%A5%EC%9D%B8%EB%AC%BC'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

#변수
charAll = []
speechAll = []
speechSel = []
speechCar = []
charPer = []
charCar = []
charTable = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > div > table')

#등장인물 추출하기
for i in charTable:
    tdAll = i.findAll('td')
    for td in tdAll:
        charAll.append(td.text)

#등장인물 선별 나용찬 ~ 수오 캡쳐카까지
charAll = charAll[4:]

#등장인물 배틀 멘트 전부
rawSpeech = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > blockquote')

#배틀 멘트 리스트 변환
for idx, s in enumerate(rawSpeech,0):
    strongAll = s.findAll('strong')
    for strong in strongAll:
        a = strong.text
        speechAll.append(a)

#등장인물 배틀 멘트 정리
for i in range(0,len(speechAll),3):
    speechSel.append(speechAll[i])
speechSel.__delitem__(-1)
speechSel.append('결코 물러서지 않겠다! 타이니소어 고!!')

#캡쳐가 배틀 멘트
for i in range(2,len(speechAll),3):
    speechCar.append(speechAll[i])

print(' 채집가 배틀멘트 '.center(40,'-'))
k = 0
for i in range(len(speechSel)):
    print('%s'.ljust(10,'.') %(charAll[k])+ '%s'.rjust(5) %(speechSel[i]))
    k += 2
print()

print(' 캡쳐가 배틀멘트 '.center(40,'-'))
k = 1
for i in range(len(speechCar)):
    print('%s'.ljust(10,'.') %(charAll[k])+ '%s'.rjust(2) %(speechCar[i]))
    k += 2

print()

nowTiny = []
rawTiny = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > ul > li > p')

for idx, i in enumerate(rawTiny,0):
    nowTiny.append(i.text)
nowTiny = nowTiny[2:44]
nowTiny.insert(15,' ')

#채집가 타이니소어 보유 현황
print(' 채집가 타이니소어 보유 현황 '.center(80,'='))
nowTinySel = []
k = 0
for i in range(0,len(nowTiny),7):
    nowTinySel.append(nowTiny[i])
    n = len(nowTiny[i].split(','))
    print('%s의 타이니소어 : %s마리 \n%s' %(charAll[k], n, nowTiny[i]))
    k = k + 2
    print(''.center(86,'='))



# for idx, i in enumerate(nowTiny,0):
#     print(idx, i)