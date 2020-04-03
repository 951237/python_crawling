from selenium import webdriver
from selenium.common.exceptions import *
from time import sleep


URL = 'https://www.culture.go.kr/sso/login.do?agentId=5'

DOWNLOAD_DIR = '/Users/mac/Documents/python_work/my_project/crawling/크롤링_나라장터_200202/imgs '
driver = webdriver.Chrome('/Users/mac/Documents/python_work/my_project/crawling/chromedriver_mac')    # 맥용 크롬드라이버 추가
driver.get(URL)

def excute_script(script):
    while True:
        try:
            driver.execute_script(script)
            break
        except JavascriptException:
            sleep(1)

# 로그인 하기
driver.find_element_by_css_selector("input#id").send_keys("s951237") #아이디입력
driver.find_element_by_css_selector("input#pw").send_keys("sji16069**") # 비밀번호 입력
excute_script("javascript:userIdStatusCheck();") # 로그인버튼 클릭
sleep(0.5)

driver.switch_to_window("공공누리") # 팝업창이 떠서 공공누리 홈페이지 브라우저 선택


# 폰트페이지 이동
driver.get('http://www.kogl.or.kr/recommend/recommendDivView.do?recommendIdx=9501&division=font')
sleep(0.5)
excute_script("javascript:recomOpenPop('popDownload_File');") #다운로드 클립
sleep(0.5)

# 팝업창 처리
driver.find_element_by_css_selector("select#useType").click() #팝업창에서 활용용도 선택
driver.find_element_by_xpath('//*[@id="useType"]/option[3]').click() #팝업창 세부용도 선택
driver.find_element_by_css_selector("input#agree").click() # 개인정보 이용 동의
excute_script("javascript:recomDownloadFile('9500');") # 다운로드 클릭
sleep(0.5)
