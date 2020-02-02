import urllib.request
import bs4

url = "https://media.daum.net/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

box_headline = bs_obj.find("div",{"id":"cMain"})
headlines = box_headline.findAll("ul",{"class" : "list_headline"})

# strong_tag = [headline.find_all("strong") for headline in headlines]
#
# print(strong_tag[])
for i  in range(3):
    for head in headlines[i]:
        strong_tag = head.find("strong")
        strong = [strong_tag]
        print(strong)
# print(headlines)