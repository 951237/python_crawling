#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup as soup

# todo 파라미터를 변수로 바꾸기
# 함수 - 태그 찾기 함수
def news_crawler01(_findTag,_findAtt,_findAll):
    _findTag = bs_obj.find("" + _findTag + "",{"id":new_id})
    _findAll = _findTag.findAll("" + _findAll + "")
    a_tag = [li.find("strong").text for li in lis]
    return  a_tag