#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 크롤링 - 다음뉴스 댓글 많은 뉴스
from urllib import request
from bs4 import BeautifulSoup

#html 파싱
url = "https://media.daum.net/"
html = request.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

# 뉴스 크롤링 - 다음 댓글많은 뉴스
def dnews_cmt():
    all_pop_cmts = bs_obj.findAll('div',{'class':'pop_news pop_cmt'})[0]
    title = all_pop_cmts.find('h3')
    all_a = all_pop_cmts.findAll('a',{'class':'link_txt'})

    a = print(title.text)

    for a_tag in all_a:
        a_tag = a_tag.text.lstrip().replace("                        ","").replace("\n", "  ")
        b = print(a_tag)
    return (a, b)

def dnews_tit():
    all_pop_tit = bs_obj.findAll('div',{'class':'pop_news pop_cmt'})[1]
    title = all_pop_tit.find('h3')
    all_a = all_pop_tit.findAll('a',{'class':'link_txt'})

    a = print(title.text)

    for a_tag in all_a:
        a_tag = a_tag.text.lstrip().replace("                    ","").replace("\n", "  ")
        b = print(a_tag)
    return (a, b)

# 뉴스 크롤링 - 다음 연령별 뉴스
def dnews_age():
    all_pop_ages = bs_obj.find('div', {'class': 'pop_news pop_age'})

    ul_femal = all_pop_ages.find('ul', {'class': 'list_agenews list_female'})
    lis_news = ul_femal.findAll('a')
    i = 1

    print("Daum 연령별 인기뉴스 : 여성")
    for li in lis_news:
        print(str(10 * i) + "대 :", li.text)
        i = i + 1

    a = print("")

    b = print("Daum 연령별 인기뉴스 : 남성")
    ul_male = all_pop_ages.find('ul', {'class': 'list_agenews list_male'})
    lis_news = ul_male.findAll('a')
    i = 1
    for li in lis_news:
        c = print(str(10 * i) + "대 :", li.text)
        i = i + 1
    return (a, b, c)

# 뉴스 크롤링 - 다음 이시각 뉴스
def dnews_now():
    box_headline = bs_obj.find("div", {"class": "box_headline"})
    all_a = box_headline.find_all("a", {"class": "link_txt"})
    i = 1
    a = print("Daum 이시간 주요 뉴스")
    for a_tag in all_a:
        a_tag = a_tag.text.replace('\n', '').strip()
        b = print(str(i) + ".", a_tag)
        i = i + 1
    return (a,b) #출력값 리턴하기


dnews_now()
print("")
dnews_cmt()
print("")
dnews_age()
print("")
dnews_tit()


input()

