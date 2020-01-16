
import urllib.request
import bs4

url = "https://www.melon.com/chart/index.htm" #url주소
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")
