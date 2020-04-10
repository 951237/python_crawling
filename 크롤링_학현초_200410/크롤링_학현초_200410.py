#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

#html 파싱
url = "https://www.kipa.org/kipa/ip002/kw_hrtraining_2202.jsp"
html = request.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

def print_len(obj):
    print(len(obj))

board = bs_obj.find('div', {'class' : 'jwxe_root jwxe_board common_d_biz-board ko'})


print(board)
