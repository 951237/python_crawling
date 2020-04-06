from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
from bs4 import BeautifulSoup as soup
from urllib import request

URL = 'https://oc10.ebssw.kr/mypage/userlrn/userLrnView.do?atnlcNo=483038&stepSn=176006&lctreSn=6160609&onlineClassYn=Y&returnUrl='

def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)

driver = webdriver.Chrome("C:/Users/User/Documents/coding_python/python_crawl\chromedriver_win.exe") # 맥용 크롬드라이버 추가
driver.get(URL)
sleep(1)

# 창 전환화기
a = driver.window_handles
driver.switch_to_window(a[2])

# 페이지 소스가져오기
html = driver.page_source  # 페이지 소스 가져오기
bs_obj = soup(html, 'html.parser')  # 뷰티풀숩 오브젝트로 가져오기

# 차시별 주소 모으기
# 블럭 찾기
nav = bs_obj.find('aside', {'class' : 'navigation sidebar'})

# select : nav > ul > li
lis = nav.select('nav > ul > li > a')
print(len(lis))
dic_link_script = {}
for i in lis:
    title = i.text.strip().split('\n')[-1]
    link_script = i.get('href').split(':')[-1]
    print(title, link_script)
    dic_link_script[title] = link_script

print(dic_link_script)


# 함수 : 페이지 이동후 soup 링크 가져오기
def get_link(link_script):

    # 자바스크립트로 페이지 이동
    excute_script(link_script)
    sleep(1)

    # 페이지 소스가져오기
    html = driver.page_source  # 페이지 소스 가져오기
    bs_obj = soup(html, 'html.parser')  # 뷰티풀숩 오브젝트로 가져오기

    # 전체 블럭 선택
    divs = bs_obj.find('div', {'id': 'playerEl'})
    video = divs.select('video')
    link = video[0].get('src')
    return link


for k, v in dic_link_script.items():
    link = get_link(v)
    print(k,link)
