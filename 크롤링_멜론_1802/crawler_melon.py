import urllib.request
import bs4

url = "https://www.melon.com/chart/index.htm"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

print(bs_obj)
# melon_chart = bs_obj.find('div',{'id':'tb_list'})
# print(melon_chart)