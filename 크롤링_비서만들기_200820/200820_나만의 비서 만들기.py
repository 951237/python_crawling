import requests
from bs4 import BeautifulSoup

# 뷰티플 숩 객체 만들기
def create_soup(p_url):
    # 유저에이전트 설정 - what is my user-agent 검색
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        }

    # 링크 정보 받아오기
    res = requests.get(p_url, headers=headers)
    res.raise_for_status()  # 정보가 없으면 프로그램 종료

    soup = BeautifulSoup(res.text, "lxml")
    return soup

def today_news():
    print('=' * 25, "오늘의 뉴스", '=' * 25)
    URL = "https://news.daum.net"
    soup = create_soup(URL) #뷰티플 숩 객체 만들기
    news = soup.find("ol", attrs={"class" : "list_popcmt"}).find_all("li") #뉴스목록 선택
    for i, item in enumerate(news[:3]): # 뉴스목록 5개중에서 3개만 선택
        title = item.find('a', attrs={"class": "link_txt"}).get_text().replace("                            ",
                                        "")[4:].strip() # 뉴스 기사
        link = item.find('a', attrs={"class": "link_txt"})['href'] #뉴스 링크
        from_news = item.find('span', attrs={"class":"info_news"}).get_text() #뉴스 출처(방송사 및 신문사)
        print(f'{i+1}위: {title}({from_news}) / {link}') # 출력하기
    print()

def today_weather():
    print('=' * 25, "오늘의 날씨", '=' * 25)
    URL = "https://n.weather.naver.com/today/02590140" #네이버 날씨
    soup = create_soup(URL)
    div = soup.find("div", attrs={"class" : "today_weather"}) #날씨 전체 구쳑 선택
    weather_area = div.find("div", attrs={"class" : "weather_area"}) # 오늘의 날씨 요약 선택
    # 날씨 한줄 정리
    summary = weather_area.find("p", {"class" : "summary"}).get_text().strip().replace('\n'," / ")
    # 날씨 상태
    current_degree = weather_area.find("strong", attrs={
        "class":"current"}).get_text() # 현재온도
    degree_height = weather_area.find("strong", attrs={
        "class":"degree_height"}).get_text() # 최고온도
    degree_low = weather_area.find("strong", attrs={
        "class":"degree_low"}).get_text() #최저온도
    degree_feel = weather_area.find("strong", attrs={
        "class":"degree_feel"}).get_text() #체감온도
    newline = '\n'
    print(f'날씨 요약 : {summary}{newline}오늘의 온도 : {degree_height} / {degree_low} / {degree_feel}')

    ttl_areas = div.find_all('div', attrs={"class":"ttl_area"}) # 세부날씨 정보
    charts = div.find_all('div', attrs = {"class" : "chart"}) # 세부날씨 수치

    #미세먼지
    dust = ttl_areas[1].find("em", {"class" : "level_text"}).get_text()
    value = charts[0].find("strong", {"class":"value"}).get_text()

    #초미세먼지
    cho_dust = ttl_areas[2].find("em", {"class" : "level_text"}).get_text()
    cho_value = charts[1].find("strong", {"class":"value"}).get_text()

    #자외선
    sun = ttl_areas[3].find("em", {"class" : "level_text"}).get_text()
    sun_value = charts[2].find("strong", {"class":"value"}).get_text()

    print(f'미세먼지 : {dust}({value}) / 초미세먼지 : {cho_dust}({cho_value}) / 자외선 : '
          f'{sun}({sun_value}) ', '\n')

def today_english():
    print('=' * 25, "오늘의 영어회화", '=' * 25)
    URL = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(URL)
    #오늘의 회화 주제
    title = soup.find("div", attrs={"class" : "conv_titleTxt"}).get_text().strip().replace("\n", "")
    # 회화 지분 선택(영어, 한글)
    texts = soup.find_all("div", attrs={"class" : "conv_txt"})
    kor_texts = texts[0].find_all('span', attrs={"class" : "conv_sub"}) #한글 지문
    eng_texts = texts[1].find_all('span', attrs={"class" : "conv_sub"}) #영어 지문
    print(title)
    # 영어지문 출력
    for txt in eng_texts:
        print(txt.get_text())
    print()

    # 한글 지문 출력
    for txt in kor_texts:
        print(txt.get_text())
if __name__ == "__main__":
    today_news()
    today_weather()
    today_english()