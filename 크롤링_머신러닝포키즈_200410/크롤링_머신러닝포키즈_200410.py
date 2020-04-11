#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as soup
from selenium import webdriver
from time import sleep
import pandas as pd
import datetime

url = 'https://machinelearningforkids.co.uk/#!/worksheets'


def get_page_selenium(url):  # 웹드라이버 가동
    driver = webdriver.Chrome()
    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")

    # 페이지를 오브젝트로 변환
    print('페이지를 파싱중..')
    print()
    bs_obj = soup(res, 'html.parser')
    # driver.quit() # 웹드라이버 끄기
    return bs_obj, driver





# 셀레니엄으로 웹페이지 파싱. 리퀘스트 페이지 로딩 불가.
bs_obj, driver = get_page_selenium(url)


def print_len(obj):
    print(len(obj))


# 블럭 찾기
block = bs_obj.find('div', {'class': 'worksheets ng-scope'})
divs = block.find_all('div', {'class': 'worksheetcard ng-scope'})


# div = block.find('div', {'class': 'worksheetcard ng-scope'})


def get_result(div):
    # 제목과 내용 추출
    result = {} # 결과를 담을 딕셔너리
    info = div.find('div', {'class': 'cardmain'})   # 블럭 찾기
    title = info.find('div', {'class': 'title'}).text   # 제목
    summary_01 = info.find('div', {'class': 'description ng-binding'}).text # 내용 1
    summary_02 = info.find('div', {'class': 'summary ng-binding'}).text # 내용 2

    # 난이도와 유형 추출
    difficulty = div.find('div', {'class': 'difficulty ng-binding'}).text   # 난이도
    type = div.find('span', {'class': 'worksheettype ng-scope'}).text   # 인식유형

    print(f'제목 : {title}')
    print(f'내용 : {summary_01} {summary_02}')
    print(f'{difficulty} / 유형 : {type}')
    print()


# 파일링크 가져오기기
def get_download_link():
    def get_soup():
        html = driver.page_source
        bs_obj = soup(html, 'html.parser')
        return bs_obj

    bs_obj_popup = get_soup()  # 팝업창 html 소스 읽기
    table_popup = bs_obj_popup.find('div', {'class': 'md-dialog-content'})  # 팝업창 블럭 잡기
    divs_popup = table_popup.select('div > div.ng-scope')  # 파업장의 다운로드 포함 블럭 선택
    list_file_title = ['교사용 안내서', '학생용 풀버전', '학생용 숏버전', '학생용 유사프로젝트']   # 링크 제목 / 링크 내용과 맞지 않을 수 있음.

    k = 0
    print('자료 다운로드 링크')
    for i in divs_popup[0:4]:
        if i.find('a') != None:     # a태그가 있으면 실행
            link = i.find('a').get('href')  # a 태그 찾고 링크 가져오기
            print(f'{list_file_title[k]} : {link}')
        else:   # a태그가 없으면 실행
            print('링크 없음')
        k += 1  # 리스트를 순서대로 출력하기 위한 카운터
    print()

t = 1   # 다운로드 버튼 클릭을 위한 카운터
sec = 5     # 자바스크립트 실행 후 대기 시간

print('머신러닝 포 키즈 수업내용')
for div in divs:
    sleep(1)
    get_result(div)   # 교육내용 크롤링
    if t != 12:     # 12번째 자료는 링크로 동영상이 있어서 예외처리
        if t in [2, 14, 29]:    # 특이한 케이스 모음
            driver.find_element_by_xpath(f"/html/body/div/div/div[4]/div[{t}]/div[3]/div[4]/a").click()  # 다운로드 버튼 클릭
            sleep(sec)
        else:
            driver.find_element_by_xpath(f"/html/body/div/div/div[4]/div[{t}]/div[3]/div[3]/a").click()  # 다운로드 버튼 클릭
            sleep(sec)

        get_download_link()     # 링크 모음 함수 실행
        driver.find_element_by_xpath('/html/body/div/div[3]/md-dialog/md-toolbar/div/button').click()   # 팝업창 끄기 클릭
        sleep(sec)
    else:
        pass

    t += 1

driver.quit()   # 셀레니엄 끄기

