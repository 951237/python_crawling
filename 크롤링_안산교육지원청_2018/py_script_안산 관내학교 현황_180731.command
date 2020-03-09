#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import bs4

url ="http://www.goeas.kr/USR/ORG/MNU9/SchoolList.do?orgType=Z"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')

all_nowSc = bs_obj.find('table',{'class':'wtl pre-table'})
all_tr = all_nowSc.findAll('tr')

# print(all_tr)

list_tr = []

# 태그를 텍스트로 바꾸어서 리스트로 변환
for tr in all_tr:
    tr_text = tr.text.replace('\n','    ').strip()
    print(tr_text)

input()