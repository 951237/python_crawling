#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup

html = request.urlopen('https://namu.wiki/w/%ED%95%9C%ED%9A%A8%EC%A3%BC')

bs_obj = soup(html,'html.parser')

div = bs_obj.find('div',{'class':'wiki-table-wrap table-right'})
all_p = div.select('p')
list_p = []

for p in all_p:
    p_text = p.text.strip()
    list_p.append(p_text)

list_p.remove('')
list_p.remove('')
print(list_p)
# 2개씩 나눠서 출력
div = 2
# colors를 colors_copy로 복사
list_p_copy = list_p[:]
# 임시 리스트 - templist 선언
templist = []
# 반복문 color in colors:
for color in list_p:
    # 만약 colors의 갯수가 분할의 수보다 작으면
    if list_p.__len__() < div:
        # 사본 컬러 출력
        print(':'.join(list_p_copy))
        # 나가rl
        break

    # 임시리스트에 컬러 추가
    templist.append(color)

    # colors_copy에서 color삭제
    list_p_copy.remove(color)

    # 만약 임시리스트의 갯수가 분할수와 같으면
    if templist.__len__() == div:
        # 임시리스트 출력
        print(':'.join(templist))

        # 임시리스트 초기화
        templist = []

        # 만약 color_copy의 수가 분할 수보다 작거나 같으면
        if list_p_copy.__len__() <= div:
            # 만약 color_copy가 비어 있지 않다면
            if list_p_copy != []:
                # color_copy 출력
                print(':'.join(list_p_copy))
            # 나가기
            break

    # 아니면:
    else:
        continue
    # 계속하기

