#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#안산교육지원청 교육장 이름 알아내기 #180731

import urllib.request
import bs4

url ="http://www.goeas.kr/USR/ORG/MNU5/OrgList.do"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')
# print(bs_obj)

boss1_name = bs_obj.find('p',{'class':'p1 name'})
boss2_name = bs_obj.find('p',{'class':'p2 name'})
boss3_name = bs_obj.find('p',{'class':'p3 name'})

print(boss1_name.text)
print(boss2_name.text)
print(boss3_name.text)

input()