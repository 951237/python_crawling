from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep
from bs4 import BeautifulSoup as soup
from urllib import request


def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)


dic_grade = {
    "1학년": "wiseLogCommon.clickDataSend('20');fnSearchList(1, '', '', '');",
    "2학년": "wiseLogCommon.clickDataSend('21');fnSearchList(2, '', '', '');",
    "3학년": "wiseLogCommon.clickDataSend('22');fnSearchList(3, '', '', '');",
    "4학년": "wiseLogCommon.clickDataSend('23');fnSearchList(4, '', '', '');",
    "5학년": "wiseLogCommon.clickDataSend('24');fnSearchList(5, '', '', '');",
    "6학년": "wiseLogCommon.clickDataSend('25');fnSearchList(6, '', '', '');"
}

dic_semestar = {
    "1학기": "clickLogConvert(2,0);fnSearchList('', 1, '', '');",
    "2학기": "clickLogConvert(2,1);fnSearchList('', 2, '', '');"
}

URL = 'http://www.i-scream.co.kr/user/main/MainPage.do'

driver = webdriver.Chrome(
    '/Users/mac/Documents/python_work/my_project/crawling/chromedriver_mac')  # 맥용 크롬드라이버 추가
driver.get(URL)
sleep(1)

# 로그인
driver.find_element_by_css_selector("input#id").send_keys(
    input('아이디 입력 : '))  # 아이디입력
driver.find_element_by_css_selector("input#pw").send_keys(
    input('패스워드 입력 : '))  # 비밀번호 입력
excute_script("wiseLogCommon.clickDataSend('131');login();")  # 로그인 버튼 클릭
sleep(1)

# 페이지 이동 - 교과활동
driver.get('http://www.i-scream.co.kr/user/subject/SubjectChasiList.do')  #

test_onclick = "wiseLogCommon.clickDataSend('20');fnSearchList(1, '', '', '');"


# 학년 선택
def get_soup(onclick):
    excute_script(onclick)  # 교과활동 - 1학년 선택
    sleep(2)
    html = driver.page_source  # 페이지 소스 가져오기

    bs_obj = soup(html, 'html.parser')  # 뷰티풀숩 오브젝트로 가져오기

    return bs_obj


def get_subject_list(onclick):
    bs_obj = get_soup(onclick)

    # 0.학기, 단원명 링크 가져오기
    nav = bs_obj.find('nav', {'id': 'SkipToLNB'})

    # 2. 단원명과 링크 가져오기
    lis = nav.select("ul > li > a")

    sub_links = {}
    for li in lis:
        a = li.text.strip()
        onclick = li.get("onclick")
        if onclick.split('.')[0] == 'wiseLogCommon':
            sub_links[a] = onclick
    return sub_links


def display_contents(sub_links, f):
    for k, v in sub_links.items():
        print(f'{k} 출력합니다.')
        bs_obj = get_soup(v)
        tab_area = bs_obj.find('div', {'class': 'tab_area'})  # 단원 전체 영역 찾기
        # titles = tab_area.select("div > a > strong")
        contents = tab_area.select("div > ul > li > ul > li > a")

        for i in contents:
            print(i.text.strip(), file=f)
        print("", file=f)
    print("", file=f)

f = open('/Users/mac/Documents/python_work/my_project/crawling/크롤링_아이스크림_과목별 내용_200404/교과목 주제모음.txt','w')

for k, v in dic_grade.items():
    print(f'{k} 정보를 수집합니다.','\n')
    excute_script(v)
    for kk, vv in dic_semestar.items():
        print(f'{kk} 내용을 수집합니다.')
        sub_links = get_subject_list(vv)
        display_contents(sub_links, f)

f.close()





# 단원 영역에서 차시 추출하기
for div in div_all:

    lis = div.select("div > ul > li > ul > li")
    for li in lis:
        text = li.text.strip()
        print(text)

    title = div.find('a').text.strip().split()  # 단원명 추출하기, 여백을 없애고, 빈칸으로 나누
    print(' '.join(title))  # 빈칸으로 나뉘어진 텍스틀 리스트를 뛰어쓰기로 출력하기

    li_all = div.select("li")
    for i in li_all:
        print(i.find('a').text.strip())
    print()

# # 1. 학기 선택하기
# semesters = nav.select("ul > li > ol > li > a")
# for i in semesters:
#     s = i.text.strip()
#     t = i.get("onclick")
#     print(s, t)
