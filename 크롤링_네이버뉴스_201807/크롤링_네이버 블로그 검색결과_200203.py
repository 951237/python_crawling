import requests
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import time
import csv

pageNum = 1
cnt = 1
search_keyword = input('검색어를 입력하시오 : ')
hdr = {'User-Agent' : 'Mozilla/5.0'}

lastNum = int(input('몇 페이지를 검색할가요? ')) * 10 - 1

search_list = []

while pageNum < lastNum:
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0' \
        f'&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query' \
        f'={urllib.parse.quote_plus(search_keyword)}&sm=tab_pge&srchby=all&st=sim' \
        f'&where' \
        f'=post&start={pageNum}'

    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, 'html.parser')

    total = soup.select('.sh_blog_title._sp_each_url._sp_each_title')

    print(f'{cnt }페이지를 검색합니다.')
    for i in total:
        temp = []
        temp.append(i.attrs['title'])
        temp.append(i.attrs['href'])
        search_list.append(temp)
    pageNum += 10
    cnt += 1
    time.sleep(0.5)

print(f'{search_keyword }검색 결과를 {int(lastNum+1)}개 저장합니다.')
with open(f'naver_blog_search_result_{search_keyword}.csv', 'w',
          encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['제목', '링크'])
    writer.writerows(search_list)
print('작업완료!')
