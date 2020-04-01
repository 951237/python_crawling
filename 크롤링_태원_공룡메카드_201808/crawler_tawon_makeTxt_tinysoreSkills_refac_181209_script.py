#!/usr/bin/env python
# coding: utf-8

# ## 공룡메카드 배틀기술 정리

from bs4 import BeautifulSoup
from selenium import webdriver
import time


url = 'https://namu.wiki/w/%ED%83%80%EC%9D%B4%EB%8B%88%EC%86%8C%EC%96%B4#s-4'
list_tinyskill = []

def get_page(): #웹드라이버 가동
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def arrange_html(p_driver): #페이지에서 불필요한 부분 없애고 필요한 부분만 추출
    res = driver.execute_script("return document.documentElement.outerHTML")

    # 페이지를 오브젝트로 변환
    print('페이지를 파싱중..')
    print()
    bsObj = BeautifulSoup(res, 'html.parser')
    len(bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div'))
    all = bsObj.select('body > div.content-wrapper > article > div.wiki-content.clearfix > div > div')
    
    print('공룡기술 부분만 선택 합니다.')
    print()
    target = all[58] #공룡 기술이 들어있는 리스트 부분
    target_p = target.select('p') # p만 골라서 저장
    
    print('불필요한 부분은 리스트에서 삭제함.')
    print()
    del target_p[2],target_p[0] #필요없는 설명부분과 공백 삭제. 끝에서 삭제를 해야 순서가 바뀌지 않음.
    driver.quit()
    
    return target_p


def make_dic(p_target, p_list): #타이니소어와 기술들을 사전으로 만들기
    k = 0
    for i in range(int(len(p_target)/9)):
        dic = {
        'name' : p_target[k].text,
        'skill_1' : p_target[k + 1].text,
        'skill_1_desc' : p_target[k + 2].text,
        'skill_2' : p_target[k + 3].text,
        'skill_2_desc' : p_target[k + 4].text,
        'skill_3' : p_target[k + 5].text,
        'skill_3_desc' : p_target[k + 6].text,
        'skill_4' : p_target[k + 7].text,
        'skill_4_desc' : p_target[k + 8].text
        }
        p_list.append(dic)
        k = k + 9
    return p_list


def make_txt(p_list): #파일 생성하기
    print('파일을 생성중...')
    print()
    txt_file = open('tinyskill_181209.txt', 'w')
    for i in p_list:
        txt_file.write('%s \n' % (i['name']))
        txt_file.write('\t 기술 1. %s : %s \n' %(i['skill_1'], i['skill_1_desc']))
        txt_file.write('\t 기술 2. %s : %s \n' %(i['skill_2'], i['skill_2_desc']))
        txt_file.write('\t 기술 3. %s : %s \n' %(i['skill_3'], i['skill_3_desc']))    
        txt_file.write('\t 기술 4. %s : %s \n' %(i['skill_4'], i['skill_4_desc']))    
        txt_file.write('\n')
    txt_file.close()
    print('작업완료..')


# #### 실행문

driver = get_page()
time.sleep(2)
target = arrange_html(driver)
time.sleep(2)
list_tinyskill = make_dic(target, list_tinyskill)
make_txt(list_tinyskill)


# In[ ]:




