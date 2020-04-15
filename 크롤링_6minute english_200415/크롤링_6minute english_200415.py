#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 크롤링 - 6 minute english 크롤링

#라이브러리 호출
from urllib import request
from bs4 import BeautifulSoup

#html 파싱
BASE_URL = 'https://www.bbc.co.uk/'
URL = "https://www.bbc.co.uk/learningenglish/english/features/6-minute-english"
html = request.urlopen(URL)
bs_obj = BeautifulSoup(html, "html.parser")

def print_len(obj):
    print(len(obj))


# 데이터 수집하기(제목 / 링크 / 날짜)
block = bs_obj.find('div', {'class' : 'widget-container widget-container-full'})
divs = block.find_all('div', {'class' : 'text'})

for div in divs:
    title = div.find('h2').text.strip()
    link = div.find('a').get('href')
    LINK = f'{BASE_URL}{link}'
    date = div.find('h3').find('b').text.strip()
    print(title, LINK, date)
    print()
