#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 크롤링 - 다음뉴스 댓글 많은 뉴스
from urllib import request

from bs4 import BeautifulSoup

url = "https://media.daum.net/"
html = request.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

all_pop_cmts = bs_obj.find('div',{'class':'pop_news pop_cmt'})
title = all_pop_cmts.find('h3')
all_a = all_pop_cmts.findAll('a',{'class':'link_txt'})

print(title.text)
for a_tag in all_a:
    a_tag = a_tag.text.replace('\n',"").strip()
    print(a_tag)

# 결과물의 1위와 기사사의 공백을 없애는 방법은?
# 리스트 내에서 공백을 제거해야 할텐데 어떻게 해야할까?
# 파이선 스크립트를 알프레드에서 실행시키는 방법은????