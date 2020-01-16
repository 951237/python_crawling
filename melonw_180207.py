#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python자동화 #웹크롤링 멜론 라이브, 일일, 주간 선택하기 #180225

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# 목록 선택하기
choice = {
    '1': 'live/',
    '2': 'day/',
    '3': 'week/'
}


# 선택값 전달하기
def print_choice():     #선택 화면에 뿌리기
    for i in sorted(choice):
        print('{}. {}'.format(i, choice[i]))

    ch = input('Enter your choice (1-3) : ')
    return choice[ch]


# 선택값에 따라 url값 전달하기
def change_letter(_choice):     #선택에 따라 URL을 리턴
    if _choice == "live/":
        url = 'http://www.melon.com/chart/index.htm'
    else:
        url = 'http://www.melon.com/chart/' + _choice + 'index.htm'
    return url


# 다이나믹 웹크로링 #웹드라이버
def get_type(url):
    driver = webdriver.Chrome()
    driver.get(url)
    res = driver.execute_script("return document.documentElement.outerHTML")        #느낀점 html문서 소스로 바꾸기
    driver.quit()

    soup = BeautifulSoup(res, 'html.parser')

    box = soup.find('div', {'class': 'service_list_song'})

    all_song = box.find_all('tr', {'class': 'lst50'})
    return all_song


'''
def _for(i):
	title = songs.find('div', {'class' : 'ellipsis rank01'}).text.replace('\n','').strip()
	singer = songs.find('span', {'class' : 'checkEllipsis'}).text.replace('\n','').strip()
	albume = songs.find('div', {'class' : 'ellipsis rank03'}).text.replace('\n','').strip()
	print("%s위. %s / 가수 : %s / 앨범 : %s" % (i, title, singer, albume))
'''


def print_song(all_song):
    for i, songs in enumerate(all_song, 1):
        # 25위까지 출력하기
        if i < 26:
            title = songs.find('div', {'class': 'ellipsis rank01'}).text.replace('\n', '').strip()
            singer = songs.find('span', {'class': 'checkEllipsis'}).text.replace('\n', '').strip()
            albume = songs.find('div', {'class': 'ellipsis rank03'}).text.replace('\n', '').strip()
            print("%s위. %s / 가수 : %s / 앨범 : %s" % (i, title, singer, albume))
        # 26위에서 멈추고, 26위 출력하기
        elif i == 26:
            input("Press any key.......")
            title = songs.find('div', {'class': 'ellipsis rank01'}).text.replace('\n', '').strip()
            singer = songs.find('span', {'class': 'checkEllipsis'}).text.replace('\n', '').strip()
            albume = songs.find('div', {'class': 'ellipsis rank03'}).text.replace('\n', '').strip()
            print("%s위. %s / 가수 : %s / 앨범 : %s" % (i, title, singer, albume))
        # 50위까지 출력하기
        elif i < 51:
            title = songs.find('div', {'class': 'ellipsis rank01'}).text.replace('\n', '').strip()
            singer = songs.find('span', {'class': 'checkEllipsis'}).text.replace('\n', '').strip()
            albume = songs.find('div', {'class': 'ellipsis rank03'}).text.replace('\n', '').strip()
            print("%s위. %s / 가수 : %s / 앨범 : %s" % (i, title, singer, albume))

    # print()


# 함수들 묶기
def song():
    _choice = print_choice()
    print('데이터를 불러 오고 있습니다...')
    url = change_letter(_choice)
    all_song = get_type(url)
    print_song(all_song)


song()

# print(box.prettify())