#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 미국의 주와 수도를 사전으로 만들기 : 문제 소스 만들기

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://ko.wikipedia.org/wiki/미국의_주'

driver = webdriver.Chrome()
print('사이트에 접속중..')
driver.get(url)

# 페이지 소스 가져오기
res = driver.execute_script("return document.documentElement.outerHTML")

driver.close()

# 페이지를 오브젝트로 변환
bsObj = BeautifulSoup(res, 'html.parser')

# 페이지 중에서 원하는
allTrs = bsObj.select('#mw-content-text > div > table.wikitable.sortable.jquery-tablesorter > tbody > tr')

# 리스트 만들기
state = []

# 모든 내용을 리스트로 만들기
for tr in allTrs:
    state.append(tr.text)

# 수
stateSub = []

# 줄단위로 끊어서 리스트 만들기
for i in state:
    i = i.split('\n')
    stateSub.append(i)

# 리스트에서 딕셔너리 만드는 방법 #느낀점 {x[i]:x[i+1] for i in range(0,len(x),2)}

# 주의 이름과 수도의 내용으로 사전 만들기
dicState = {stateSub[i][1]: stateSub[i][4] for i in range(0, len(stateSub))}
