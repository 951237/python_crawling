#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 미국의 주와 수도를 사전으로 만들기 : 문제 소스 만들기

from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://ko.wikipedia.org/wiki/미국의_주'

driver = webdriver.Chrome()
print('사이트에 접속중..')
driver.get(url)

# 페이지 소스 가져오기
res = driver.execute_script("return document.documentElement.outerHTML")

driver.close()

# 페이지를 오브젝트로 변환
bsObj = BeautifulSoup(res, 'html.parser')

# 페이지 중에서 원하는
allTrs = bsObj.select('#mw-content-text > div > table.wikitable.sortable.jquery-tablesorter > tbody > tr')

# 리스트 만들기
state = []

# 모든 내용을 리스트로 만들기
for tr in allTrs:
    state.append(tr.text)

# 수
stateSub = []

# 줄단위로 끊어서 리스트 만들기
for i in state:
    i = i.split('\n')
    stateSub.append(i)

# 리스트에서 딕셔너리 만드는 방법 #느낀점 {x[i]:x[i+1] for i in range(0,len(x),2)}

# 주의 이름과 수도의 내용으로 사전 만들기
dicState = {stateSub[i][1]: stateSub[i][4] for i in range(0, len(stateSub))}

## 문제파일 만들고 순서 바꾸기

import random

# 35개 문제지 파일 만들기
for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # 문제지 헤더 작성하기
    quizFile.write('Name : \n\nDate : \n\nPeride : \n\n')
    quizFile.write(('   ' * 20) + 'state Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # 미국 주의 순서 섞기
    listState = list(dicState.keys())
    random.shuffle(listState)

    # 50개의 주를 반복하여 각각의 문제 만들기
    for questionNum in range(50):

        # 정답과 오답 만들기
        correctAnswer = dicState[listState[questionNum]]
        wrongAnswer = list(dicState.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)

        # 문제파일에 문제와 선택답안 쓰기
        quizFile.write('%s. %s의 수도는 무엇입니까?\n' % (questionNum + 1, listState[questionNum]))
        for i in range(4):
            quizFile.write('      %s. %s\n' % ('ㄱㄴㄷㄹ'[i], answerOption[i]))
        quizFile.write('\n')

        # 파일에 문제의 답 기록하기
        answerFile.write('%s. %s\n' % (questionNum + 1, 'ㄱㄴㄷㄹ'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
