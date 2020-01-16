#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#태원 타이니소어 배틀 기술 정리 #180820

#알고리즘
'''
1. 페이지 파싱
2. 단락 선택하기
3.
'''


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://namu.wiki/w/%ED%83%80%EC%9D%B4%EB%8B%88%EC%86%8C%EC%96%B4#s-4'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

char_list = [] #캐릭터 리스트
battle_list = [] #캐릭터 배틀 기술 리스트
discription_list = [] #캐릭터 배틀 기술 설명 리스트

#타이니소어 캐릭터가 든 소스 모두 가져오기
char = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > ul')
for i in char:
    char_list.append(i.text)

#캐릭터 기술 모두 가져오기
battle = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > blockquote')
for i in battle:
    battle_list.append(i.text)

#캐릭터 기술 설명 가져오기
discription = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div > p')
for i in discription:
    discription_list.append(i.text)

#캐릭터만 슬라이싱
char_list = char_list[55:94]

#배틀기술만 슬라이싱
battle_list = battle_list[0:156]

#배틀 설명만 슬라이싱
discription_list = discription_list[107:263]

#캐릭터 1개에 배틀기술, 배틀 설명 1대 1로 매칭
'''
01. 티라노
    1. 기술 1 : 기술1 설명
    2. 기술 2 : 기술2 설명
    3. 기술 3 : 기술3 설명
    4. 기술 4 : 기술4 설명

02. 트리케라톱스
    1. 기술 1 : 기술1 설명
    2. 기술 2 : 기술2 설명
    3. 기술 3 : 기술3 설명
    4. 기술 4 : 기술4 설명
'''
out = open('tinysore.txt','w')
k = 0
for i in range(len(char_list)):
    print(char_list[i],file=out)
    for j in range(int(len(battle_list)/39)):
        print('\t 기술 %s. %s : %s' %(j+1, battle_list[k], discription_list[k]),file=out)
        k = k + 1
out.close()

#참고 파일저장하기
'''
out = open('data.txt','w') #파일생성
print("출력내용",file=out) #출력결과를 파일로 기록
out.close() #파일닫기
'''

#참고 순위매겨서 출력하기, 넘버링
'''
for idx, title in enumerate(discription_list,0):
    print('%s. %s' %(idx,title))

for idx, title in enumerate(title_list,1): #넘버링, 순위매기기
    _a = print("{} {}{}{}".format('자료명',idx,'.',title.text.replace('\n','').strip()),file=out) #출력하기 - 폼에 맞게
'''


# 참고 @눕이 제작 실시간 검색순위 파싱 soup.select 이요
'''
def realRank_Nup():
    #soup selct - 클래스의 span값이 ah_k인 것을 고르기
    title_list = bs_obj.select('.PM_CL_realtimeKeyword_rolling_base span[class*=ah_k]')

    for idx, title in enumerate(title_list,1): #넘버링, 순위매기기
        _a = print("{}{} {}".format(idx,'위',title.text)) #출력하기 - 폼에 맞게
    return (_a)

realRank_Nup()
'''