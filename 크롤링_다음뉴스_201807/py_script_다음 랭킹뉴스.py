#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj

url = 'https://media.daum.net/ranking/popular/'
bs_obj = get_html(url)

def dnew_rank_pop():
    all_news = bs_obj.find('div',{'class':'rank_news'})
    # print(len(all_news))
    title = all_news.find('h4')
    all_a = all_news.findAll('a',{'class':'link_txt'})

    a = print(title.text)

    i = 1
    for a_tag in all_a:
        print(f'{i}위 : {a_tag.text}')
        print()
        i += 1

dnew_rank_pop()
input()



