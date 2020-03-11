#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request

from bs4 import BeautifulSoup as soup

from datetime import datetime

url = 'http://ghostmecard.choirock.com/character.php'


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj


bs_obj = get_html(url)

# 캐릭터 팝업창 정보 수
popups = bs_obj.findAll('div', {'class': 'popup_info'})


def make_dic(popups):
    # 12지신 정보만 수집 < 배경 >의 특징이 있음.
    _list = []
    for popup in popups:
        srcs = popup.text.replace('                    	', "").split('\n')
        if '< 배경 >\r' in srcs:
            _dic = {
                'name': srcs[1],
                'disc': srcs[2:]
            }
            _list.append(_dic)
    return _list


def show_contents(_list):
    for lst in _list:
        print(lst['name'])  # 12지 정령 이름 출력
        for a in lst['disc']:  # 12지 정령 내용 출력
            print(a.replace('\r', ""))
        print()


def make_text(_list):
    file_name = f'태원_요괴메카드_12지신_{datetime.now()}.txt'
    print(f'{file_name} 파일 작성 시작!')
    txt_file = open(file_name, 'w')
    for lst in _list:
        nl = '\n'
        tb = '\t'
        _r = '\r'
        txt_file.write(f'{lst["name"]}{nl}') #12정령 이름 작성
        for a in lst["disc"]:   # 12지 정령 내용 기록 시작
            txt_file.write(f'{tb}{a.replace(_r, "")}{nl}')
        txt_file.write(f'{nl}')
    txt_file.close()
    print(f'{file_name} 파일 작성 완료!')


_list = make_dic(popups)    # 딕셔너리 생성
show_contents(_list)    # 화면 출력하기
# make_text(_list)      # 파일 저장하기
