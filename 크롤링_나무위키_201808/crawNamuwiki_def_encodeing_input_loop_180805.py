#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse #url을 파라미터로 받을 때 사용하기 parse
from bs4 import BeautifulSoup as soup
#todo 그냥 엔터 입력시 까지 무한 검색하기
while True:
    name = input('궁금한 연예인의 프로필은? ')
    if name != '':
        def namuCrawl(name):
            enName = parse.quote(name)
            html = request.urlopen('https://namu.wiki/w/%s' %(enName))

            bs_obj = soup(html,'html.parser')

            #todo 모든 연예인의 클래스가 똑같지 않음. 소스 코드 수정하기
            div = bs_obj.find('div',{'class':'wiki-table-wrap table-right'})
            all_p = div.select('p')
            list_p = []

            for p in all_p:
                p_text = p.text.strip()
                if p.text != '':
                    list_p.append(p_text)
                else:
                    list_p.append(p_text)
                    list_p.remove('') #첫번째 공백 삭제
            return(list_p)

        def listSlice(_num):
            # 2개씩 나눠서 출력
            div = _num
            # colors를 colors_copy로 복사
            list_p_copy = list_p[:]
            # 임시 리스트 - templist 선언
            templist = []
            # 반복문 color in colors:
            for color in list_p:
                # 만약 colors의 갯수가 분할의 수보다 작으면
                if list_p.__len__() < div:
                    # 사본 컬러 출력
                    print(' : '.join(list_p_copy))
                    # 나가rl
                    break

                # 임시리스트에 컬러 추가
                templist.append(color)

                # colors_copy에서 color삭제
                list_p_copy.remove(color)

                # 만약 임시리스트의 갯수가 분할수와 같으면
                if templist.__len__() == div:
                    # 임시리스트 출력
                    print(' : '.join(templist))

                    # 임시리스트 초기화
                    templist = []

                    # 만약 color_copy의 수가 분할 수보다 작거나 같으면
                    if list_p_copy.__len__() <= div:
                        # 만약 color_copy가 비어 있지 않다면
                        if list_p_copy != []:
                            # color_copy 출력
                            print(' : '.join(list_p_copy))
                        # 나가기
                        break

                # 아니면:
                else:
                    # 계속하기
                    continue

        list_p = namuCrawl(name)
        listSlice(2)
        print("")
    else:
        break
