#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import bs4
ansan_part = {'A':'초등교육지원과','B':'중등교육지원과','C':'평생교육지원과','D':'경영지원과','E':'학교현장지원과','F':'교유시설과'}

for k, v in ansan_part.items(): #사전을 이용하여 여러개의 변수를 사용 #어썸
    url ="http://www.goeas.kr/USR/ORG/MNU6/OrgDetail.do?orgType=" + k + "" #문자열에 변수 넣는 방법 큰따옴표로 끊기
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, 'html.parser')

    container = bs_obj.find('div',{'id':'main_container'})
    all_tbody = container.findAll('tbody')

    list_tbody = []

    for tbody in all_tbody:
        tbody_text = tbody.text.replace('\t','').replace('\r','').replace('\n',' ')
        list_tbody.append(tbody_text)

    print(str(v))

    for tbody in list_tbody:
        print(tbody)

    print("")

out.close()