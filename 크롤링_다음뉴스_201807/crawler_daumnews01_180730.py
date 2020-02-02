#!/usr/bin/env python3
# 다음 이시간 주요 뉴스 크롤링 #180730

import urllib.request
import bs4

url = "https://media.daum.net/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

box_headline = bs_obj.find("div",{"class":"box_headline"})
all_a = box_headline.find_all("a",{"class" : "link_txt"})
i = 1
print("Daum 이시간 주요 뉴스")
for a_tag in all_a:
    a_tag = a_tag.text.replace('\n','').strip()
    print(str(i) + ".",a_tag)
    i = i + 1

