#!/usr/bin/env python3
#180730 크롤링_네이버 이시간 뉴스
import urllib.request
import bs4

url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")


def news_crawler(new_id):
    ul = bs_obj.find("ul",{"id":new_id})
    lis = ul.findAll("li")
    a_tag = [li.find("strong").text for li in lis]
    return  a_tag

news_fir = news_crawler("text_today_main_news_801001")
news_sec = news_crawler("text_today_main_news_428288")

i = 1
print("이시각 주요 뉴스")
order = [news_fir, news_sec]
for j in range(2):
    for news in order[j]:
        print(str(i) + ".", news)
        i = i + 1

# for news in news_fir:
#     print(str(i) + ".", news)
#     i = i + 1
#
# for news in news_sec:
#     print(str(i) + ".", news)
#     i = i + 1
#
# print("---------------------------")