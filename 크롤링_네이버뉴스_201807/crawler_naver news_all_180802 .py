#!/usr/bin/env python3

#180801 크롤링_네이버 모두 출력

import urllib.request
import bs4

i = 1
url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

# 뉴스 아이디 사전 만들기
all_new_id = {'이시각 주요 뉴스_섹션1':'text_today_main_news_801001',
              '이시각 주요 뉴스_섹션2':'text_today_main_news_428288',
              '정치 뉴스':'section_politics',
              '경제 뉴스':'section_economy',
              '사회 뉴스':'section_society',
              '생활/문화 뉴스':'section_life',
              '세계 뉴스':'section_world',
              'IT 뉴스':'section_it'
              }

# 이시각 주요뉴스 크롤링 - ul 태그 찾기
def news_crawler01(new_id):
    ul = bs_obj.find("ul",{"id":new_id})
    lis = ul.findAll("li")
    a_tag = [li.find("strong").text for li in lis]
    return  a_tag

# 정치, 경제, 생활, 세계, 아이티 뉴스 크롤링 - div 태그 찾기
def news_crawler02(new_id):
    ul = bs_obj.find("div",{"id":new_id})
    lis = ul.findAll("li")
    b_tag = [li.find("strong").text for li in lis]
    return  b_tag

# 키값과 밸류 값을 비교하면서 조건에 맞게 뉴스 크롤링
for _ti, _id in all_new_id.items():
    i = 1                           # 뉴스의 번호를 섹션별로 초기화, 만약 지운다면 전체뉴스에 대해서 넘버링
    if _ti == '이시각 주요 뉴스_섹션1': #키값이 '이시각 주요 뉴스 섹션1'과 같으면
        news_sec = news_crawler01(_id) # 크롤러1에 밸류값을 입력하여 뉴스 크롤링
    elif _ti == '이시각 주요 뉴스_섹션2':
        news_sec = news_crawler01(_id)
    else:
        news_sec = news_crawler02(_id)
    print(_ti)
    for news in news_sec:
        print(i,news)
        i = i + 1
    print("---------------"*5)