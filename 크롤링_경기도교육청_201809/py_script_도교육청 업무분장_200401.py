from urllib import request
from bs4 import BeautifulSoup as soup
from datetime import date  # 날짜 호출하기

def write_date():
    mayday = date.today()  # 오늘 날짜 저장하기
    return mayday.strftime('%y%m%d')

today = write_date()

# 북부 납부 부서 링크 가져오기
jiyuk = ['02','25']
list_part = []
list_link = []
# out = open(f'kyungGi_people_{today}.txt','w', encoding='utf8')

for ji_i in jiyuk:
    url = 'http://www.goe.go.kr/edu/organ/selectWorkList.do?organId=' + ji_i + '00000000000&menuId=270151203155925&programId=PGM_1000000010'

    html = request.urlopen(url)
    bs_obj = soup(html,'html.parser')

    dl = bs_obj.find('dl',{'class':'forWeb'})
    all_a = dl.select('a')

    # 부서명과 링크 가져오기
    for a in all_a:
        part = a.text
        href = a.get('href') # href속성값만 가지고 오기, 낱개에서만 작동함. 리스트에서는 안됨. 반복문을 돌릴때 사용
        list_part.append(part)
        list_link.append(href)

# todo

for link_i in list_link:
    url = 'http://www.goe.go.kr' + link_i + ''

    html = request.urlopen(url)
    bs_obj = soup(html,'html.parser')

    div = bs_obj.find('div',{'class':'mBoard1'})

    thead = div.find('thead')
    all_tr = div.findAll('tr')

    list_tr = []
    for tr in all_tr:
        tr_text = tr.text.replace('\n',' ').replace('\t','').replace('\r','').strip()
        list_tr.append(tr_text)

    for tr in list_tr:
        # print(tr,file=out)
        print(tr, "\n")

    print("===" * 40, "\n")

input()
# out.close()
