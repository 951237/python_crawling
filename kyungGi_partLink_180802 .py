#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

from bs4 import BeautifulSoup as soup

jiyuk = ['02','25']
list_part = []
list_link = []

for ji_i in jiyuk:
    url = 'http://www.goe.go.kr/edu/organ/selectWorkList.do?organId=' + ji_i + '00000000000&menuId=270151203155925&programId=PGM_1000000010'

    html = request.urlopen(url)
    bs_obj = soup(html,'html.parser')

    dl = bs_obj.find('dl',{'class':'forWeb'})
    all_a = dl.select('a')

    # todo 부서명과 링크 가져오기
    for a in all_a:
        part = a.text
        href = a.get('href') # href속성값만 가지고 오기, 낱개에서만 작동함. 리스트에서는 안됨. 반복문을 돌릴때 사
        list_part.append(part)
        list_link.append(href)
        # print(part,href)

    # print('----------'*10)
print(list_part)
print(list_link)