#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request

import requests
from bs4 import BeautifulSoup as soup
import datetime
import  os.path

URL = 'http://ghostmecard.choirock.com/character.php'
BASE_URL = 'http://ghostmecard.choirock.com'
테이머 = []
tabs = {
    'tab1': '테이머',
    'tab2': '십이지정령',
    'tab3': '수호정',
    'tab4': '요괴',
    'tab5': '왕마요괴'
}


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj


bs_obj = get_html(URL)

# 캐릭터 세부정보 수집
popups = bs_obj.findAll('div', {'class': 'popup_info'})

# 이미지 링크 수집하
def get_link(imgs):
    for img in imgs:
        dic = {
            'name': img.get('alt'),
            'link': img.get('src')
        }
    return dic

# 테이머 이름과 이미지 링크 수집
for k, v in tabs.items():
    _list = []
    ids = bs_obj.find('div', {'id': k})
    imgs = ids.findAll('img')
    dic = {v : get_link(imgs)}
    테이머.append(dic)


# 이미지 파일 저장하기
def download_img(_list):
    for i in _list:
        name = i['name']
        link = BASE_URL + i['link']

        # 파일이름 = 경로 + 파일이름
        filename = os.path.join(f'/Users/mac/Documents/python_work/my_project/crawling/크롤링_요괴메카드/{name}', f'{name}.png')

        # 파일저장 경로가 없으면, 폴더 생성 있으면, 그냥 패스~
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as file:
            response = requests.get(link, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break
                file.write(block)

for t in 테이머:
    download_img(t)

# 캐릭터 세부정보 수집 popups
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


# 캐릭터 정보 화면 출력
def show_contents(_list):
    for lst in _list:
        print(lst['name'])  # 12지 정령 이름 출력
        for a in lst['disc']:  # 12지 정령 내용 출력
            print(a.replace('\r', ""))
        print()


# 캐릭터 정보 텍스트파일 저장하기
def make_text(_list):
    file_name = f'태원_요괴메카드_12지신_{datetime.now()}.txt'
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

# _list = make_dic(popups)    # 딕셔너리 생성
# show_contents(_list)    # 화면 출력하기
# make_text(_list)      # 파일 저장하기
