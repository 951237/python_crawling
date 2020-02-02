#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

import bs4

f = open('ansan_ES_180731.txt','w')

url ="http://www.goeas.kr/USR/ORG/MNU9/SchoolList.do?orgType=B"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')

all_eleSc = bs_obj.find('table',{'class':'dtl'})
all_td = all_eleSc.findAll('td')

list_td = []

# 태그를 텍스트로 바꾸어서 리스트로 변환
for td in all_td:
    td_text = td.text.replace('\n','').strip()
    list_td.append(td_text) #결과값을 리스트에 추가하기

print("구분  /", "학교명     /", '주소                 /', '교무실        /', '행정실        /', '팩스',file=f)
# 리스트를 6개씩 분할하여 출력하기
start_pos = 0
end_pos = len(list_td)
div = 6

for i in range(start_pos,end_pos+div,div): #i는 왜 사용된지 잘 이해가 안됨.
    out = list_td[start_pos:start_pos+div]
    if out != []:
            print(' / '.join(out),file=f) #리스트를 문자열로 변환
    start_pos = start_pos + div

f.close()
