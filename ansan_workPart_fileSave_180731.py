#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#안산교육지원청 과별 업무분장 크롤링 #180731

import urllib.request
import bs4
ansan_part = {'A':'초등교육지원과','B':'중등교육지원과','C':'평생교육지원과','D':'경영지원과','E':'학교현장지원과','F':'교유시설과'}


out = open('ansan_workpart_180801.txt','w')

for k, v in ansan_part.items(): #사전을 이용하여 여러개의 변수를 사용 #어썸
    print('%s의 정보 불러오고 있습니다.' %(v))
    print()
    url ="http://www.goeas.kr/USR/ORG/MNU6/OrgDetail.do?orgType=" + k + "" #문자열에 변수 넣는 방법 큰따옴표로 끊기
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, 'html.parser')

    container = bs_obj.find('div',{'id':'main_container'})
    all_tbody = container.findAll('tbody')

    list_tbody = []


    for tbody in all_tbody:
        tbody_text = tbody.text.replace('\t','').replace('\r','').replace('\n',' ')
        list_tbody.append(tbody_text)

    print('%s의 정보 기록하는 중...' %(v))
    print()
    print(str(v),file=out)

    for tbody in list_tbody:
        print(tbody,file=out)

    print("",file=out)

out.close()