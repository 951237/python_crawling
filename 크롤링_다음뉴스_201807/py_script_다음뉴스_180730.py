#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 최종 수정 20.04.10

# 크롤링 - 다음뉴스 댓글 많은 뉴스
from urllib import request
from bs4 import BeautifulSoup

#html 파싱
url = "https://media.daum.net/"
html = request.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

# 뉴스 크롤링 - 다음 열독률 높은 뉴스
def dnews_cmt():
    all_pop_cmts = bs_obj.findAll('div',{'class':'pop_news pop_cmt'})[0]
    title = all_pop_cmts.find('h3')
    lis  = all_pop_cmts.select('ol > li')
    print(title.text, '\n')

    for li in lis[:6]:
        content = li.find_all('span')
        rank = content[0].text
        source = content[1].text
        link = li.find('a').get('href')
        txt = li.text.strip().replace("                    ","").replace("\n", "  ").replace("         "," :").replace("       "," /")
        print(txt, link)


# 댓글 많은 뉴스
def dnews_tit():
    all_pop_tit = bs_obj.findAll('div',{'class':'pop_news pop_cmt'})[1]
    title = all_pop_tit.find('h3').text
    lis = all_pop_tit.select('ol > li')

    print(title,'\n') # 댓글많은 뉴스 출력


    for li in lis[:6]:
        content = li.find_all('span')
        rank = content[0].text
        source = content[1].text
        link = li.find('a').get('href')
        txt = li.text.strip().replace("                    ", "").replace("\n", "  ").replace("         ", " :").replace(
            "       ", " /")
        print(txt, link)

# 뉴스 크롤링 - 다음 연령별 뉴스
def dnews_age():
    all_pop_ages = bs_obj.find('div', {'class': 'pop_news pop_age'})
    dic_gener = {
        '여성' : 'list_agenews list_female',
        '남성' : 'list_agenews list_male'
    }

    for k, v in dic_gener.items():
        ul_femal = all_pop_ages.find('ul', {'class': v})
        lis_news = ul_femal.findAll('a')
        i = 1

        print(f'Daum 연령별 인기뉴스 : {k}','\n')
        for li in lis_news:
            txt = li.text
            link = li.get('href')
            print(f'{str(10 * i + 10)}대 : {li.text} / {link}')
            i = i + 1
        print("")


# 뉴스 크롤링 - 다음 이시각 뉴스
def dnews_now():
    box_headline = bs_obj.find("div", {"class": "box_headline"})
    lis = box_headline.select('ul > li')

    print("Daum 이시간 주요 뉴스", '\n')
    i = 1
    for li in lis[:6]:
        content = li.find_all('strong')
        txt = content[0].text.strip().replace('\n'," / ")
        link = li.find('a').get('href')
        print(f'{i}. {txt} / {link}')
        i += 1


dnews_now()
print("")
dnews_cmt()
print("")
dnews_age()
print("")
dnews_tit()


input()

