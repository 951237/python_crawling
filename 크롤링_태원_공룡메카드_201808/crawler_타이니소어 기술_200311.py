#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as soup
from selenium import webdriver
import pandas as pd
import datetime

url = 'https://namu.wiki/w/%ED%83%80%EC%9D%B4%EB%8B%88%EC%86%8C%EC%96%B4#s-4'
list_tiny = []


def get_page_selenium(url):  # 웹드라이버 가동
    driver = webdriver.Chrome()
    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")

    # 페이지를 오브젝트로 변환
    print('페이지를 파싱중..')
    print()
    bs_obj = soup(res, 'html.parser')
    driver.quit()
    return bs_obj


# 셀레니엄으로 웹페이지 파싱. 리퀘스트 페이지 로딩 불가.
bs_obj = get_page_selenium(url)

all = bs_obj.findAll('div', {'class': 'wiki-heading-content'})

# 배틀 기술 부분 선택- 56번째
contents = all[56].findAll('div', {'class': 'wiki-paragraph'})

del contents[2]  # 여백 삭제
del contents[0]  # 가장 처음 주석 삭제

# 함수 - 사전 만들기
def make_dic(contents):
    i = 0
    for k in range(int(len(contents) / 9)):
        # 이중 딕셔너리
        dic = {
            contents[i].text: {
                '스킬 1': contents[i + 1].text,
                '설명 1': contents[i + 2].text,
                '스킬 2': contents[i + 3].text,
                '설명 2': contents[i + 4].text,
                '스킬 3': contents[i + 5].text,
                '설명 3': contents[i + 6].text,
                '스킬 4': contents[i + 7].text,
                '설명 4': contents[i + 8].text
            }
        }
        list_tiny.append(dic)
        i += 9
    return list_tiny

# 타이니소어 기술 화면 출력
def show_skills(list_tiny):
    i = 0
    for tiny in list_tiny:
        for k, v in tiny.items():
            print(k)
            print(f'스킬 1. {list_tiny[i][k]["스킬 1"]} : {list_tiny[i][k]["설명 1"]}')
            print(f'스킬 2. {list_tiny[i][k]["스킬 2"]} : {list_tiny[i][k]["설명 2"]}')
            print(f'스킬 3. {list_tiny[i][k]["스킬 3"]} : {list_tiny[i][k]["설명 3"]}')
            print(f'스킬 4. {list_tiny[i][k]["스킬 4"]} : {list_tiny[i][k]["설명 4"]}')
            i += 1
        print()

def make_txt(list_tiny):
    print('파일을 생성중...')
    print()
    txt_file = open(f'태원_타이니소어 기술_{datetime.datetime.now()}.txt', 'w')
    i = 0
    nl = '\n'
    tb = '\t'
    for tiny in list_tiny:
        for k, v in tiny.items():
            txt_file.write(f'{k}{nl}')
            txt_file.write(f'{tb}스킬 1. {list_tiny[i][k]["스킬 1"]} : {list_tiny[i][k]["설명 1"]}{nl}')
            txt_file.write(f'{tb}스킬 2. {list_tiny[i][k]["스킬 2"]} : {list_tiny[i][k]["설명 2"]}{nl}')
            txt_file.write(f'{tb}스킬 3. {list_tiny[i][k]["스킬 3"]} : {list_tiny[i][k]["설명 3"]}{nl}')
            txt_file.write(f'{tb}스킬 4. {list_tiny[i][k]["스킬 4"]} : {list_tiny[i][k]["설명 4"]}{nl}')
            txt_file.write(f'{nl}')
            i += 1
    txt_file.close()
    print('작업완료!')

list_tiny = make_dic(contents)
show_skills(list_tiny)
make_txt(list_tiny)



