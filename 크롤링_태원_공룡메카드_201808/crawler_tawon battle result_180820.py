#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 태원 - 타이니소어 배틀 정리 #180820

#알고리즘
'''
1. 페이지 파싱
2. 단락 선택하기
3.
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://namu.wiki/w/%ED%83%80%EC%9D%B4%EB%8B%88%EC%86%8C%EC%96%B4#s-4'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

char_list = []
result_list = []

a = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > div > table')
c = bsObj.select('h3')
k = 0
for i in a:
    td = i.findAll('td')
    for j in td:
        char_list.append(j.text)


char = char_list[9:40]
char.remove('23.암모') #암모 리스트에서 삭제
char.remove('25.아노말로') #아노말로 리스트에서 삭제
result = char_list[42:266]

#'상대'값을 가진 인덱스를 리스트 만들기
k = 0
list_n = []
for idx, title in enumerate(result,0):
    if title == '상대':
        list_n.append(idx)
    else:
        continue

print(len(char))


#공룡 이름 출력후, 배틀 결과 출력
i = 0
k = 0
m = 0
for i in range(len(list_n)):
    if i == 29:
        exit()
    print(' %s의 배틀 '.center(30, '-') %(char[m])) #가운데 정렬
    j = 0
    while j < int(list_n[i+1] - list_n[i]):
        print('%s'.ljust(25, '.') %(result[k]) + '%s'.rjust(5) %(result[k+1])) #왼쪽, 오른족 정렬
        j += 2
        k += 2
    print()
    m += 1
