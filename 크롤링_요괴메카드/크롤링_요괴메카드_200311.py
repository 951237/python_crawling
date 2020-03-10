#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request

from bs4 import BeautifulSoup as soup

url = 'http://ghostmecard.choirock.com/character.php'


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj


bs_obj = get_html(url)

# 캐릭터 팝업창 정보 수
popups = bs_obj.findAll('div', {'class': 'popup_info'})
_list = []

# 12지신 정보만 수집 < 배경 >의 특징이 있음.
for popup in popups:
    srcs = popup.text.replace('                    	', "").split('\n')
    if '< 배경 >\r' in srcs:
        _dic = {
            'name': srcs[1],
            'disc': srcs[2:]
        }
        _list.append(_dic)

# for lst in _list:
#     print(lst['name'])
#     for a in lst['disc']:
#         print(a.replace('\r', ""))
#     print()

for lst in _list:
    txt_file = open('태원_요괴메카드_12지신.txt', 'w')
    nl = '\n'
    tb = '\t'
    _r = '\r'
    txt_file.write(f'{lst["name"]}{nl}')
    for a in lst["disc"]:
        txt_file.write(f'{tb}{a.replace(_r, "")}{nl}')
    txt_file.write(f'{nl}')
    txt_file.close()
