#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

from bs4 import BeautifulSoup as soup

src = 'https://media.daum.net/ranking/popular'

base = 'https://media.daum.net'


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj


bs_obj = get_html(src)
all_news = bs_obj.find('div', {'class': 'rank_news'})

# 랭킹 url 구하기
def get_url(all_news):
    tab_nav2 = all_news.find('ul', {'class': 'tab_nav tab_nav2'})
    links = tab_nav2.findAll('a', {'class': 'link_tab'})
    dic_links = {}
    for a in links[1:]:
        name = a.text.strip()
        link = a.get('href')
        dic_links[name] = link
    return dic_links


# 랭킹 뉴스의 제목 구하
def get_news(all_news):
    title = all_news.find('h4')
    all_a = all_news.findAll('a', {'class': 'link_txt'})

    a = print(title.text)

    i = 1
    for a_tag in all_a:
        print(f'{i}위 : {a_tag.text}')
        i += 1


get_news(all_news)

# 많이본 뉴스 출력
urls = get_url(all_news)
print()

for k, v in urls.items():
    if k != '열독률 높은':
        bs_obj = get_html(base+v)
        # print(base+v)
        all_news = bs_obj.find('div', {'class': 'rank_news'})
        get_news(all_news)
        print()
