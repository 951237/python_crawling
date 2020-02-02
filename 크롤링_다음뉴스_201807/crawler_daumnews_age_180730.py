#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 다음뉴스 연령별 인기뉴스
from urllib import request
from bs4 import BeautifulSoup

url = "https://media.daum.net/"
html = request.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

all_pop_ages = bs_obj.find('div',{'class':'pop_news pop_age'})

ul_femal = all_pop_ages.find('ul',{'class':'list_agenews list_female'})
lis_news = ul_femal.findAll('a')
i = 1

print("Daum 연령별 인기뉴스 : 여성")
for li in lis_news:
    print(str(10*i) + "대 :", li.text)
    i = i + 1

print("")

print("Daum 연령별 인기뉴스 : 남성")
ul_male = all_pop_ages.find('ul',{'class':'list_agenews list_male'})
lis_news = ul_male.findAll('a')
i = 1
for li in lis_news:
    print(str(10*i) + "대 :", li.text)
    i = i + 1
