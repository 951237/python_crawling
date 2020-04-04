from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep

def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)


URL = 'http://www.i-scream.co.kr/user/main/MainPage.do'

driver = webdriver.Chrome('/Users/mac/Documents/python_work/my_project/crawling/chromedriver_mac')    # 맥용 크롬드라이버 추가
driver.get(URL)

# 로그인
driver.find_element_by_css_selector("input#id").send_keys(input('아이디 입력 : ')) # 아이디입력
driver.find_element_by_css_selector("input#pw").send_keys(input('패스워드 입력 : ')) # 비밀번호 입력
excute_script("wiseLogCommon.clickDataSend('131');login();") #로그인 버튼 클릭

# 1학년 이동
excute_script("wiseLogCommon.clickDataSend('114');") #교과활동 이동