#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

url = 'http://www.edunet.net'

# 함수 - bs4로 html 가져오기
driver = webdriver.Chrome()
driver.get(url)
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

bs_obj = BeautifulSoup(res, 'html.parser')

print(bs_obj)