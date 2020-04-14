from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
from bs4 import BeautifulSoup as soup


BASE_URL = 'http://www.kogl.or.kr/'
URL = 'https://www.culture.go.kr/sso/login.do?agentId=5'


driver = webdriver.Chrome('/Users/mac/Documents/python_work/my_project/crawling/chromedriver_mac')    # 맥용 크롬드라이버 추가
driver.get(URL)

def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)

input("계속하려면 엔터키를 누르시오.")


# 글꼴 페이지 주소 가져오기
html = driver.page_source
bs_obj = soup(html, 'html.parser')

# 글꼴페이지 링크 가져오기
block = bs_obj.select('ul.recommend-list > li > div.subject')

dic_link = {}
for i in block:
    title = i.text.strip()
    link = i.find('a').get('href')
    LINK = f'{BASE_URL}{link}'
    dic_link[title] = LINK
    print(title, LINK)

print(dic_link)



# 글꼴 다운로드 받기
excute_script("javascript:recomOpenPop('popDownload_File');") #다운로드 클
sleep(0.5)
# 팝업창 처리
print('다운로드창에 정보를 입력합니다.')
driver.find_element_by_css_selector("select#useType").click() #팝업창에서 활용용도 선택
driver.find_element_by_xpath('//*[@id="useType"]/option[3]').click() #팝업창 세부용도 선택
driver.find_element_by_css_selector("input#agree").click() # 개인정보 이용 동의
excute_script("javascript:recomDownloadFile('9500');") # 다운로드 클릭
sleep(0.5)
