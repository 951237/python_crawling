import requests
from bs4 import BeautifulSoup
from noti import send

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

def today_english():
    result =[]
    main_title = ('=' * 25, "오늘의 영어회화", '=' * 25)
    result.append(main_title)
    URL = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(URL)
    #오늘의 회화 주제
    title = soup.find("div", attrs={"class" : "conv_titleTxt"}).get_text().strip().replace("\n", "")
    # 회화 지분 선택(영어, 한글)
    texts = soup.find_all("div", attrs={"class" : "conv_txt"})
    kor_texts = texts[0].find_all('span', attrs={"class" : "conv_sub"}) #한글 지문
    eng_texts = texts[1].find_all('span', attrs={"class" : "conv_sub"}) #영어 지문
    # print(title)
    result.append(title)
    # 영어지문 출력
    # print('영어 대화')
    result.append('영어 대화')
    for txt in eng_texts:
        # print(txt.get_text())
        i = txt.get_text()
        result.append(i)
    # print()

    # 한글 지문 출력
    print('한글 대화')
    result.append('한글 대화')
    for txt in kor_texts:
        # print()
        i = txt.get_text()
        result.append(i)
    return result

data = today_english()
send(data)