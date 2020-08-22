#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 과학창의재단 연수 신청에서 개인정보수정중 소속학교 찾기 및 선택 버튼이 보이지 않아 셀레니엄으로 해결함.

from selenium import webdriver

URL = 'http://lms.kofac.re.kr'

# 사이트 접속하기
driver = webdriver.Chrome('/Users/mac/Documents/coding_python/python_crawling/chromedriver_mac')
print('사이트에 접속중..')
driver.get(URL)

# 로그인 및 기타 세세한 것은 수기 입력으로 해결
# 선택버튼이 바로 클릭되지 않아, 우회해서 클릭(출처 : 스택오버플로)
element = driver.find_element_by_xpath('//*[@id="schoolList"]/li[1]/dl/dd/a')
driver.execute_script("arguments[0].click();", element)