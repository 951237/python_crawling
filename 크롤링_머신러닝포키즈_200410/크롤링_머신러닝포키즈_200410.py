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
    result = {}
    info = div.find('div', {'class': 'cardmain'})
    title = info.find('div', {'class': 'title'}).text
    summary_01 = info.find('div', {'class': 'description ng-binding'}).text
    summary_02 = info.find('div', {'class': 'summary ng-binding'}).text

    # 난이도와 유형 추출
    difficulty = div.find('div', {'class': 'difficulty ng-binding'}).text
    type = div.find('span', {'class': 'worksheettype ng-scope'}).text

    print(f'제목 : {title}')
    print(f'내용 : {summary_01}{summary_02}')
    print(f'{difficulty} / 유형 : {type}')
    print()


def download_files(i):
    sec = 4
    driver.find_element_by_xpath(f'/html/body/div/div/div[4]/div[{i}]/div[3]/div[3]/a').click()
    sleep(sec)
    driver.find_element_by_xpath('//*[@id="dialogContent_22"]/div/div[2]/div[1]/a').click()
    sleep(sec)
    driver.find_element_by_xpath('//*[@id="dialogContent_22"]/div/div[2]/div[2]/div[2]/a').click()
    sleep(sec)
    driver.find_element_by_xpath('//*[@id="dialogContent_22"]/div/div[2]/div[3]/div[2]/a').click()
    sleep(sec)
    driver.find_element_by_xpath('//*[@id="dialogContent_22"]/div/div[2]/div[4]/div[2]/a').click()
    sleep(sec)
    driver.find_element_by_xpath('/html/body/div/div[3]/md-dialog/md-toolbar/div/button/md-icon').click()
    sleep(sec)



i = 1
print('머신러닝 포 키즈 수업내용')
for div in divs:
    # get_result(div)   # 교육내용 크롤링
    download_files(i) # 워크시트 다운로드
    sleep(2)
    i += 1
