#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import os.path
from urllib import request

import requests
from bs4 import BeautifulSoup as soup

URL = 'http://ghostmecard.choirock.com/character.php'  # 요괴메카드 캐릭터 소개 페이지
BASE_URL = 'http://ghostmecard.choirock.com'  # 이미지 파일다운 앞부분 주소
테이머 = []  # 카테고리, 캐릭터 이름, 이미지 주소 담기 위한 리스트

# 각 카테고리별 이동위한 웹페이지 id 값
tabs = {
    'tab1': '테이머',
    'tab2': '십이지정령',
    'tab3': '수호정령',
    'tab4': '요괴',
    'tab5': '왕마요괴'
}


# 뷰티플솦 오브젝트 소스 가져오
def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    print('페이지 소스 로딩 완료!')
    return bs_obj


bs_obj = get_html(URL)

# 캐릭터 세부정보 수집
popups = bs_obj.findAll('div', {'class': 'popup_info'})


# 이미지 링크 수집하기(캐릭터 이름, 이미지 주소)
def get_link(imgs, dics):
    for img in imgs:
        name = img.get('alt')  # alt 속성 가져오기
        link = img.get('src')  # src 속성 가져오기
        dics[name] = link  # 딕셔너리에 이름/링크 넣기
    print('캐릭터 이름 및 링스 수집 완료!')
    return dics


# 실행문 - 테이머 이름과 이미지 링크 수집
for k, v in tabs.items():
    _list = []  # 전체 딕셔너리 담기 위한 리스트
    _dic = {}  # 캐릭터 이름과, 주소 담을 딕셔너리
    ids = bs_obj.find('div', {
        'id': k})  # div의 id값(tab) 찾기, 페이지 이동하기(테이머, 십이지정령, 왕마요괴등등)
    imgs = ids.findAll('img')  # img 모두 찾기
    dic = get_link(imgs, _dic)  # 이름, 링크 모으기 함수 실행
    테이머.append({v: dic})  # 리스트에 담기


# 링크 파일 저장하기
def save_file(filename):
    os.makedirs(os.path.dirname(filename),
                exist_ok=True)  # 파일저장 경로가 없으면, 폴더 생성 있으면, 그냥 패스~
    with open(filename, 'wb') as file:  # 파일 열기, 윈도우에서 encoding='utf-8' 고려하기
        response = requests.get(link, stream=True)  # 링크 살아있는지 확인

        if not response.ok:  # 링크가 유효하지 않으면 상태 출력
            print(response)

        for block in response.iter_content(
                1024):  # 1024 파일 단위로 쪼개서 저장하기. 파일 큰 경우 오류가 나면 다시 해야함
            if not block:
                break
            file.write(block)
    print(f'{filename} 파 저장완료!')


all_char = []  # 전체 캐릭터이름 분류하기
dic_char_name = {}  # 캐릭터 이름

for t in 테이머:
    for k, v in t.items():
        dir_name = k  # 저장폴더 이름을 카테고리로 지정(테이머, 십이지정령 .... )
        for i in range(len(v.keys())):  # 키값의 수만큼 반복하기
            _keys = list(v.keys())  # 리스트 속의 벨류 딕셔너리의 키값을 리스트로 변환, 캐릭터 이름
            _values = list(v.values())  # 리스트 속의 벨류 딕셔너리의 벨류값을 리스트로 변환, url 주소
            name = _keys[i]  # 캐릭터 이름, 파일명
            link = BASE_URL + _values[i]  # 전체 링크 주소

            # 파일이름 = 경로 + 파일이름, join 함수를 이용하여 두개를 합치기
            filename = os.path.join(
                f'/Users/mac/Documents/python_work/my_project/crawling/크롤링_요괴메카드/imgs/{dir_name}/',
                f'{name}.png')

            # save_file(filename)

            # 캐릭터 이름 리스트 생성하기
            dic_char_name[dir_name] = _keys
        all_char.append(_keys)

list_tamer = all_char[0]
list_12 = all_char[1]
list_guard = all_char[2]
list_ghost = all_char[3]
list_king_ghost = all_char[4]

list_char = [list_12, list_tamer, list_ghost, list_guard, list_king_ghost]


# 캐릭터

# 캐릭터 세부정보 수집 popups
def get_char_disc(popups, list_chars):
    _list = []
    for popup in popups:
        srcs = popup.text.replace('                    	', "").split('\n')
        이름 = srcs[1]
        설명 = srcs[2:]

        # 만약 name이 테이머에 있다면, 딕셔너리에 이름과 설명 담기
        if 이름 in list_chars:
            _list.append({'name': 이름, 'disc': 설명})
    print(f'{이름} 정보 수집 완료!')
    return _list


# 캐릭터 정보 화면 출력
def show_contents(_list):
    for lst in _list:
        print(lst['name'])  # 12지 정령 이름 출력
        for a in lst['disc']:  # 12지 정령 내용 출력
            print(a.replace('\r', ""))
        print()


# 캐릭터 정보 텍스트파일 저장하기
def make_text(_list):
    file_name = f'태원_요괴메카드_12지신_{datetime.datetime.now()}.txt'
    print(f'{file_name} 파일 작성 시작!')
    txt_file = open(file_name, 'w')
    for lst in _list:
        nl = '\n'
        tb = '\t'
        _r = '\r'
        txt_file.write(f'{lst["name"]}{nl}')  # 12정령 이름 작성
        for a in lst["disc"]:  # 12지 정령 내용 기록 시작
            txt_file.write(f'{tb}{a.replace(_r, "")}{nl}')
        txt_file.write(f'{nl}')
    txt_file.close()
    print(f'{file_name} 파일 작성 완료!')


for i in list_char:
    _list = get_char_disc(popups, i)  # 딕셔너리 생성
    show_contents(_list)  # 화면 출력하기
    make_text(_list)  # 파일 저장하기
    print()
