# crawler_naver news_fun
import urllib.request
import bs4

url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

ul = bs_obj.find("ul",{"id":"text_today_main_news_801001"})
lis = ul.findAll("li")

a_tag = [li.find("strong").text for li in lis]

    # for li in lis:
    #     a_tag = li.find("strong").text
    #     print(a_tag)

print(a_tag)



# bs4_obj = bs4.BeautifulSoup()