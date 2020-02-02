#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup

url = 'http://www.goe.go.kr/edu/organ/selectWorkList.do?organId=0200000000000&menuId=270151203155925&programId=PGM_1000000010'

html = request.urlopen(url)
bs_obj = soup(html,'html.parser')

div = bs_obj.find('div',{'class':'mBoard1'})

thead = div.find('thead')
all_tr = div.findAll('tr')

list_tr = []
for tr in all_tr:
    tr_text = tr.text.replace('\n',' ').replace('\t','').replace('\r','').strip()
    list_tr.append(tr_text)

for tr in list_tr:
    print(tr)