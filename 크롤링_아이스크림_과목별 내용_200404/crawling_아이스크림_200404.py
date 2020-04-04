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


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj

URL = 'http://www.i-scream.co.kr/user/main/MainPage.do'

driver = webdriver.Chrome('/Users/mac/Documents/python_work/my_project/crawling/chromedriver_mac')    # 맥용 크롬드라이버 추가
driver.get(URL)
sleep(1)

# 로그인
driver.find_element_by_css_selector("input#id").send_keys(input('아이디 입력 : ')) # 아이디입력
driver.find_element_by_css_selector("input#pw").send_keys(input('패스워드 입력 : ')) # 비밀번호 입력
excute_script("wiseLogCommon.clickDataSend('131');login();") #로그인 버튼 클릭
sleep(1)

# 페이지 이동 - 교과활동
driver.get('http://www.i-scream.co.kr/user/subject/SubjectChasiList.do') #

# 학년 선택
excute_script("wiseLogCommon.clickDataSend('20');fnSearchList(1, '', '', '');") # 교과활동 - 1학년 선택
html =driver.page_source # 페이지 소스 가져오기

bs_obj = soup(html, 'html.parser') # 뷰티풀숩 오브젝트로 가져오기

tab_area = bs_obj.find('div', {'class' : 'tab_area'}) # 단원 전체 영역 찾기
div_all = tab_area.findAll('div', {'class' : 'toggle_list curriculum1'}) # 단원 영역 모두 찾기

# 단원 영역에서 차시 추출하기
for div in div_all:

    title = div.find('a').text.strip().split() # 단원명 추출하기, 여백을 없애고, 빈칸으로 나누
    print(' '.join(title)) # 빈칸으로 나뉘어진 텍스틀 리스트를 뛰어쓰기로 출력하기

    li_all = div.select("li")
    for i in li_all:
        print(i.find('a').text.strip())
    print()


'''
1학년 1학기 과목 
wiseLogCommon.clickDataSend('2000');fnSearchList('', '', '237627', '','국어', 'ajax');
wiseLogCommon.clickDataSend('2003');fnSearchList('', '', '237631', '','수학', 'ajax');
wiseLogCommon.clickDataSend('20014');fnSearchList('', '', '237635', '','통합교과', 'ajax');
wiseLogCommon.clickDataSend('20020');fnSearchList('', '', '237589', '','안전한 생활', 'ajax');
wiseLogCommon.clickDataSend('20021');fnSearchList('', '', '30', '','입학 초기 적응활동', 'ajax');
wiseLogCommon.clickDataSend('20011');fnSearchList('', '', '126313', '','창의', 'ajax');
wiseLogCommon.clickDataSend('2004');fnSearchList('', '', '172627', '','교과학습 보충자료', 'ajax');

1학년 2학기 과목
wiseLogCommon.clickDataSend('2010');fnSearchList('', '', '237668', '','국어', 'ajax');
wiseLogCommon.clickDataSend('2013');fnSearchList('', '', '237669', '','수학', 'ajax');
wiseLogCommon.clickDataSend('20114');fnSearchList('', '', '237670', '','통합교과', 'ajax');
wiseLogCommon.clickDataSend('20120');fnSearchList('', '', '237589', '','안전한 생활', 'ajax');
wiseLogCommon.clickDataSend('20111');fnSearchList('', '', '126313', '','창의', 'ajax');


'''
excute_script("wiseLogCommon.clickDataSend('21');fnSearchList(2, '', '', '');") # 교과활동 - 2학년 선택
excute_script("wiseLogCommon.clickDataSend('22');fnSearchList(3, '', '', '');") # 교과활동 - 3학년 선
