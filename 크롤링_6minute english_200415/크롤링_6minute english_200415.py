#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 크롤링 - 6 minute english 크롤링

#라이브러리 호출
from urllib import request
from bs4 import BeautifulSoup

#html 파싱
BASE_URL = 'https://www.bbc.co.uk'
URL = "https://www.bbc.co.uk/learningenglish/english/features/6-minute-english"


def get_soup(URL):
    html = request.urlopen(URL)
    bs_obj = BeautifulSoup(html, "html.parser")
    return bs_obj

def print_len(obj):
    print(len(obj))


# 데이터 수집하기(제목 / 링크 / 날짜)
bs_obj = get_soup(URL)
block = bs_obj.find('div', {'class' : 'widget-container widget-container-full'})
divs = block.find_all('div', {'class' : 'text'})


dic_link = {}

for div in divs:
    title = div.find('h2').text.strip()
    link = div.find('a').get('href')
    LINK = f'{BASE_URL}{link}'
    date = div.find('h3').find('b').text.strip()
    dic_link[title] = {'link' : LINK, 'date' : date}
    # print(title, LINK, date)
    # print()

for i in dic_link:
    print(i.value)


# 자료 다운로드
dic_item = {}
bs_obj = get_soup('https://www.bbc.co.uk/learningenglish/english/features/6-minute-english/ep-21082014')
print_len(bs_obj)

# pdf 링크 수
pdf = bs_obj.find('div', {'class' : 'widget-pagelink-download-inner bbcle-download-linkparent-extension-pdf'})
link_pdf = block.find('a').get('href')

# mp3 링크 수집
mp3 = bs_obj.find('div', {'class' : 'widget-pagelink-download-inner bbcle-download-linkparent-extension-mp3'})
link_mp3 = mp3.find('a').get('href')

dic_item['link_pdf'] = link_pdf
dic_item['link_mp3'] = link_mp3

print(dic_item)