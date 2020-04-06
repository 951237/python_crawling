from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
from bs4 import BeautifulSoup as soup
from urllib import request

URL = 'http://primary.ebs.co.kr/course/series/list?seriesId=S00044'
PATH_DRIVER = "/Users/mac/Documents/python_work/my_project/crawling/chromedriver_mac"

# 웹드라이버 호출
driver = webdriver.Chrome(PATH_DRIVER)  # 맥용 크롬드라이버 추가
driver.get(URL)
sleep(1)


def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)


def print_len(obj):
    print(len(obj))


# 함수 - 단원명과 스크립트 링크수집
def get_links_script():
    # 웹페이지 소스 읽기
    html = driver.page_source  # 페이지 소스 가져오기
    bs_obj = soup(html, 'html.parser')  # 뷰티풀숩 오브젝트로 가져오기

    # 블럭 선택
    table = bs_obj.find('table', {'class': 'board_list2 lect_list_table'})
    trs = table.select('tbody > tr')

    links_script = {}
    # 영상제목, 자바스크립트 링크 수집
    for i in trs:
        td = i.find('td', {'class': 'title'})  # 제목수
        if td != None:
            title = td.text.strip()

            a = i.find('a')
            link = a['onclick']

            # print(title, link)
            links_script[title] = link
    return links_script


# 함수 - 영상 소스 가져오기
def get_video_links(onclick):
    # 자바스크립트 페이지 이동
    excute_script(onclick)
    sleep(3)

    # 페이지 소스 가져오기
    html = driver.page_source
    bs_obj = soup(html, 'html.parser')

    # 블럭잡기
    divs = bs_obj.find('div',
                       {'class': 'mpv_container skin_default mpv_playing'})
    # print(f'divs count : {print_len(divs)}')

    # 영상 링크 수집
    video = divs.select('video')
    link = video[0].get('src')
    # print(link)

    return link

# 작업 순서

# 교과목 페이지 이동
# 페이지 단원명 및 페이지 링크 수집
links_script = get_links_script()

# print(links_script)
# 비디오 링크 수집
for k, v in links_script.items():
    link = get_video_links(v)
    print(k, link)