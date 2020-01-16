#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 구글 검색 #180823

import requests, sys, webbrowser, bs4
from urllib import request, parse #url을 파라미터로 받을 때 사용하기 parse

k = []
k = input('What are you looking for? ')
enName = parse.quote(k) #입력받은 글을 인코딩함

print('Googling.....')
res = requests.get('http://google.com/search?q=' + ''.join(enName[0:]))
res.raise_for_status()

bsObj = bs4.BeautifulSoup(res.text)

linkElems = bsObj.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))