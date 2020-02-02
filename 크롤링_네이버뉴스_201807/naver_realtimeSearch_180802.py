#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup

url = 'https://www.naver.com/'

html = request.urlopen(url)
bs_obj = soup(html, 'html.parser')

# @진일 제작 실시간 검색순위 파싱
def realRank_951237():
    div = bs_obj.find('div',{'class':'ah_roll_area PM_CL_realtimeKeyword_rolling'})
    all_span = div.findAll('span','ah_k')

    for idx, span in enumerate(all_span,1): #넘버링하면서 반복하기
        s = span.text #soup을 텍스트로 바꿔주기
        # print(str(idx) + "위",s) #출력하기 - 그냥
        _a = print("{}{} {}".format(idx, '위', s)) # 출력하기 - 양식에 맞게
    return _a

# @눕이 제작 실시간 검색순위 파싱 soup.select 이요
def realRank_Nup():
    #soup selct - 클래스의 span값이 ah_k인 것을 고르기
    title_list = bs_obj.select('.PM_CL_realtimeKeyword_rolling_base span[class*=ah_k]')

    for idx, title in enumerate(title_list,1): #넘버링, 순위매기기
        _a = print("{}{} {}".format(idx,'위',title.text)) #출력하기 - 폼에 맞게
    return (_a)

realRank_Nup()