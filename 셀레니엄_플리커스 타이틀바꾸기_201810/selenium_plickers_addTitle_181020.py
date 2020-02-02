#!/usr/bin/env python
# coding: utf-8

'''
#플리커 사이트 자동화 2편
- 문제마다 단원명의 텍스트를 타이틀로 넣는 작업
- 컴퓨터로 자동화 해도 1시간 이상이 넘어간는 대작업.
- 중요한 포인트
    - 웹에서 작업은 컴퓨터에서 처럼 즉각적으로 이뤄지지 않음.
    - 페이지가 바뀔때마다 쉬는 시간을(time.sleep)를 주는 것이 중요함.
# todo 타이틀에 폴더의 문제수를 카운트해서 타이틀에 번호를 달기.
'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# 플리커 로그인
def loginPlickers():
    # res = driver.execute_script("return document.documentElement.outerHTML")
    try:
        driver.forward()
        driver.maximize_window()
        time.sleep(0.25)

        print('구글계정으로 로그인 시도..')
        driver.find_element_by_xpath('//*[@id="App"]/div/div/div[2]/button').click()

        print('계정정보 입력중..')
        input('Press Enter... ')

    except Exception as e:
        print(e)

# 라이브러리 페이지 파싱 allDiv값 반환
def parsingLibrary():
    page = 'https://www.plickers.com/library'
    driver.get(page)
    res = driver.execute_script("return document.documentElement.outerHTML")

    bs_obj = BeautifulSoup(res, 'html.parser')
    allDiv = bs_obj.select('#focusableLibraryTable')
    print('페이지 파싱 완료...')
    return allDiv

# 문제디스플레이 수정하기 / 전체 혹은 부분[시작단원 -1 : 끝단원 +1]
# ## 타이틀 넣기
    # - for i in div.find_all(class_='cellRow')[94:102]:               #원하는 부분에서 시작할때는 마지막에 [시작위치:], 전체를 실행하려면 [:] 혹은 대괄호 삭제#느낀점
    # ### 문제 수정하기 - 문서 파싱 / 단원 및 문제 아이디값 추출

def addTitle():
    print('단원과 페이지별 아이디를 출력중...')
    for div in allDiv:
        j = 1
        for i in div.find_all(class_='cellRow')[:]:
            _id = i.get('id')
            _title = i.text
            print('%s %s : %s' %(j, _title, _id))
            j = j + 1
    print('출력 완료...')

    print('문제 아이디값 추출...')
    for div in allDiv:
        for i in div.find_all(class_='cellRow')[0:3]:               #원하는 부분에서 시작할때는 마지막에 [시작위치:] #느낀점
            iID = i.get('id')                                       #5, 6학년 차시별 아이디 추출하기
            iTitle = i.text
            print('%s 단원타이틀 입력 시작' %(iTitle))
            subPage01 = 'https://www.plickers.com/library/%s' %(iID)    # 차시별 주소 구하기
            driver.get(subPage01)                                       # 차시별 사이트로 이동

            time.sleep(4)
            res = driver.execute_script("return document.documentElement.outerHTML")
            bs_objSub = BeautifulSoup(res, 'html.parser')
            allDivSub = bs_objSub.select('#focusableLibraryTable')

            for div in allDivSub:
                for i in div.find_all(class_='cellRow'):
                    count = 1       # 문제 번호 카운트
                    countAll = int(len(div.find_all(class_='cellRow'))) #단원의 전체 문제수
                    subID = i.get('id')  # 차시내 문제 아이디 추출하기
                    subIdTitle = i.text
                    #                     subPage02 = 'https://www.plickers.com/question/%s' % (subID)  # 문제 주소 구하기
                    #                     driver.get(subPage02)  # 문제로 이동

                    time.sleep(4)
                    print('\t%s 수정중...' %(subIdTitle))
                    subPage03 = 'https://www.plickers.com/editor/%s' %(subID)       # 문제 편집 사이트 주소 구하기
                    driver.get(subPage03)       # 편집주소로 이동하기

                    time.sleep(3)
                    print('\t타이틀 입력작업 시작...')
                    inputElemen = driver.find_element_by_xpath('//*[@id="questionBodyTextArea"]')
                    inputElemen.clear()
                    inputElemen.send_keys(iTitle + '(%s/%s)' % (count, countAll))
                    time.sleep(2)
                    print('')
    print('Completed...')



url = 'https://www.plickers.com/login'
page = 'https://www.plickers.com/library'

driver = webdriver.Chrome()
print('사이트에 접속중..')
driver.get(url)

loginPlickers()         #플리커 로그인

allDiv = parsingLibrary()   #플리커 라이브러리 파싱

addTitle()            #문제에 제목넣기

print('To library page...')
driver.get(page)


