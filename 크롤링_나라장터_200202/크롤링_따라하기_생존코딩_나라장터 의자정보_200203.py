import os
from io import BytesIO
from time import sleep
from urllib.request import urlretrieve as download

import lxml
import pandas as pd
from PIL import Image
from openpyxl import Workbook
from selenium import webdriver
from selenium.common.exceptions import *

DOWNLOAD_DIR = '/Users/mac/Documents/python_work/my_project/crawling/크롤링_' \
               '나라장터_200202/imgs '
# driver = webdriver.Chrome('/Users/mac/Documents/python_work/my_project'
#                          '/crawling/chromedriver_mac')    # 맥용 크롬드라이버 추가
driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\python_crawling\chromedriver_win.exe')    #윈도우용 크롬드라이버 추가
driver.get('http://shopping.g2b.go.kr')  # 나라장터 사이트로 이동
driver.switch_to.frame('sub')  # 메인프레임속의 서브프레임으로 바꾸기

driver.find_element_by_css_selector("input#kwd.srch_txt").send_keys("작업용 의자")
# 검색어 '작업용 의자'입력
driver.find_element_by_css_selector("input#kwd.srch_txt").submit()  # 검색하기


# 더보기 클릭
sleep(1)
driver.execute_script("javascript:fnGoodsAttrNmFold('show');")

# 등판재질 선택하기
필수옵션 = ['메시', '망사']
제외옵션 = '가죽'
sleep(1)
driver.execute_script("javascript:attrNmValLink('5611210201', '등판재질',  "
                      "'ATTR_269556' , '' ); ")  # 자바스크립트 코드 실행

체크박스리스트 = driver.find_elements_by_css_selector(
    'ul#dLstDiv>li>input[type="checkbox"]')  # 체크박스의 텍스트가 인풋 태그 밖에 위치하여 체크박스를 모두 찾음.

for 체크박스 in 체크박스리스트: # 왜 안될까?
    parent = 체크박스.find_element_by_xpath('./..')  # 체크박스 상위를 부모로 변수를 만듦
    for i in 필수옵션:  # 필수옵션 리스트 2개 확인
        if i in parent.text and '가죽' not in parent.text:  # '메시'나 '망사'를 포함하지만,
            # '가죽'을 포함하지 않는다면
            체크박스.click()
driver.execute_script("javascript:toSMPPIntgrSrchGoodsList('');")   #조회 버틑 클릭


# 좌판 재질 선택하기
sleep(1)
driver.execute_script("javascript:attrNmValLink('5611210201', '좌판재질',  'ATTR_264449' , '' ); ")  # 자바스크립트 코드 실행

체크박스리스트 = driver.find_elements_by_css_selector(
    'ul#dLstDiv>li>input[type="checkbox"]')  # 체크박스의 텍스트가 인풋 태그 밖에 위치하여 체크박스를 모두 찾음.

for 체크박스 in 체크박스리스트: # 왜 안될까?
    parent = 체크박스.find_element_by_xpath('./..')  # 체크박스 상위를 부모로 변수를 만듦
    for i in 필수옵션:  # 필수옵션 리스트 2개 확인
        if i in parent.text and '가죽' not in parent.text:  # '메시'나 '망사'를 포함하지만,
            # '가죽'을 포함하지 않는다면
            체크박스.click()
driver.execute_script("javascript:toSMPPIntgrSrchGoodsList('');")   #조회 버틑 클릭

# 팔걸이 유
sleep(1)
driver.execute_script("javascript:attrNmValLink('5611210201', '팔걸이유무',  'ATTR_259429' , '' ); ")  # 자바스크립트 코드 실행

체크박스리스트 = driver.find_elements_by_css_selector(
    'ul#dLstDiv>li>input[type="checkbox"]')  # 체크박스의 텍스트가 인풋 태그 밖에 위치하여 체크박스를 모두 찾음.

for 체크박스 in 체크박스리스트: # 왜 안될까?
    parent = 체크박스.find_element_by_xpath('./..')  # 체크박스 상위를 부모로 변수를 만듦
    if parent.text == '유':  # 값이 '유'이면
            체크박스.click()
driver.execute_script("javascript:toSMPPIntgrSrchGoodsList('');")   #조회 버틑 클릭

# 리스트를 100개로 정렬
sleep(1)
driver.find_element_by_css_selector('option[value = "100"]').click()
sleep(1)
driver.execute_script("javascript:searchForNewPageSize();")

# 인증검색에 우선구매대상 + 의무구매대상 체크
sleep(1)
driver.find_element_by_css_selector("input[id = 'priorObligPrdCrtfcCheck']").click()    # 체크박스 클릭
driver.execute_script("javascript:toSMPPIntgrSrchGoodsList('');")   #조회 버틑 클릭


# 검색된 의자 이미지와 정보 가져오기

아이템_리스트 = driver.find_elements_by_css_selector("tbody>tr>td>a[href^='javascript:toSMPPGoodsDtlInfo(']")     # 정규표현식 'java...'로시작하는 href태그를 수집

스크립트_리스트 = []

for i in 아이템_리스트:
    script = i.get_attribute("href")
    스크립트_리스트.append(script)

# 엑셀파일 생성하기
filename = r'C:\Users\User\PycharmProjects\python_crawling\크롤링_나라장터_200202\chair_list.xlsx'
book = Workbook()
book.save(filename)

# 내용 가져오기
with pd.ExcelWriter(filename, engine = 'openpyxl', mode = 'a') as writer:
    writer.book = book
    writer.sheets = { ws.title: ws for ws in book.worksheets }

    for idx, script in enumerate(스크립트_리스트):
        driver.execute_script(script)
        print(idx)
        sleep(1)
        spec = pd.read_html(driver.page_source, index_col=0)[0].transpose()
        if idx == 0:
            spec.columns = map(lambda a: a.replace(" :", ''), spec.columns)
            spec.to_excel(writer, startrow=0, sheet_name='Sheet', index=False)
        else:
            spec.to_excel(writer, startrow=writer.sheets['Sheet'].max_row, sheet_name='Sheet', index=False, header=False)



