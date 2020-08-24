from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
from bs4 import BeautifulSoup as soup
from urllib import request
import requests


def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)


WIN_DRIVER = "C:/Users/User/Documents/coding_python/python_crawl\chromedriver_win.exe"
MAC_DRIVER = "/Users/mac/Documents/coding_python/python_crawling/chromedriver_mac"


# -------------- 1단계 : 온라인클래스 사이트 접속 --------------------
# EBS 온라인 클래스 주소
URL = 'https://oc10.ebssw.kr/mypage/userlrn/userLrnView.do?atnlcNo=483038&stepSn=176006&lctreSn=6160609&onlineClassYn=Y&returnUrl='
driver = webdriver.Chrome(MAC_DRIVER)  # 맥용 크롬드라이버 추가
driver.get(URL)


# -------- 2단계 : 사이트 로그인 하기 및 페이지로 이동하기 ----------------
# 대기하기
input("비번 입력후 대기하기")


# 동영상이 있는 페이지 링크에서 페이지 파싱하기
target_url = "https://oc10.ebssw.kr/mypage/userlrn/userLrnView.do?atnlcNo=1641737&stepSn=245211&lctreSn=7813337&onlineClassYn=Y"
driver.get(target_url)
a = driver.window_handles
driver.switch_to_window(a[2])  # 두번째 탭으로 바꾸기
html = driver.page_source  # 페이지 소스 가져오기
bs_obj = soup(html, 'html.parser')  # 뷰티풀숩 오브젝트로 가져오기


# -------- 3단계 : 단원명 링크 수집 후 동영상 다운로드 ----------------
# 차시별 주소 모으기
# 블럭 찾기
nav = bs_obj.find('aside', {'class': 'navigation sidebar'})

# select : nav > ul > li
lis = nav.select('nav > ul > li > a')
print(len(lis))
dic_link_script = {}
for i in lis:
    title = i.text.strip().split('\n')[-1]
    link_script = i.get('href').split(':')[-1]
    print(title, link_script)
    dic_link_script[title] = link_script

    # print(dic_link_script)


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


# 링크 다운로드
def link_download(p_name, p_link): # 단원명과 링크
    # 링크 다운로드
    r = requests.get(p_link, allow_redirects=True)
    open(f'{p_name}.mp4', 'wb').write(r.content)  # 대기시간이 필요없음. 순차적으로 다운로드 됨.


# 단원명과 링크 화면 출력 다운로드
for k, v in dic_link_script.items():
    link = get_link(v)
    print(k, link)

    link_download(k, link)

print("작업완료!!!")
