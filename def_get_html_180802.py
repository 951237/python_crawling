#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup

# 함수 - bs4로 html 가져오기
def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html,"html.parser")
    return bs_obj