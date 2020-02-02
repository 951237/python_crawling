#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup

url = 'https://namu.wiki/w/%EC%A0%95%EC%9A%B0%EC%84%B1'

#나무위키에서 연예인 정보가져오기
def namuCrawl():
    html = request.urlopen(url)

    bs_obj = soup(html,'html.parser')

    div = bs_obj.find('div',{'class':'wiki-table-wrap table-right'})
    all_p = div.select('p')
    list_p = []

    for p in all_p:
        p_text = p.text.strip()
        if p.text != '':
            list_p.append(p_text)
        else:
            list_p.append(p_text)
            list_p.remove('') #첫번째 공백 삭제
    return(list_p)

#정보를 숫자대로 슬라이스 분할하여 출력하기
def listSlice(_num):
    # 2개씩 나눠서 출력
    div = _num
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
            # 계속하기
            continue

list_p = namuCrawl()
listSlice(2)
