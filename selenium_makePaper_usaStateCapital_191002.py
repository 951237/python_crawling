#!/usr/bin/env python3
# -*- coding: utf-8 -*-

capitals = {'델라웨어주': '도버  (Dover)',
 '펜실베이니아주': '해리스버그 (Harrisburg)',
 '뉴저지주': '트렌턴 (Trenton)',
 '조지아주': '애틀랜타 (Atlanta)',
 '코네티컷주': '하트퍼드 (Hartford)',
 '매사추세츠주': '보스턴 (Boston)',
 '메릴랜드주': '아나폴리스 (Annapolis)',
 '사우스캐롤라이나주': '컬럼비아 (Columbia)',
 '뉴햄프셔주': '콩코드 (Concord)',
 '버지니아주': '리치먼드 (Richmond)',
 '뉴욕주': '올버니 (Albany)',
 '노스캐롤라이나주': '롤리 (Raleigh)',
 '로드아일랜드주': '프로비던스 (Providence)',
 '버몬트주': '몬트필리어 (Montpelier)',
 '켄터키주': '프랭크퍼트 (Frankfort)',
 '테네시주': '내슈빌 (Nashville)',
 '오하이오주': '콜럼버스 (Columbus)',
 '루이지애나주': '배턴루지 (Baton Rouge)',
 '인디애나주': '인디애나폴리스 (Indianapolis)',
 '미시시피주': '잭슨 (Jackson)',
 '일리노이주': '스프링필드 (Springfield)',
 '앨라배마주': '몽고메리 (Montgomery)',
 '메인주': '오거스타 (Augusta)',
 '미주리주': '제퍼슨시티 (Jefferson City)',
 '아칸소주': '리틀록 (Little Rock)',
 '미시간주': '랜싱 (Lansing)',
 '플로리다주': '탤러해시 (Tallahassee)',
 '텍사스주': '오스틴 (Austin)',
 '아이오와주': '디모인 (Des Moines)',
 '위스콘신주': '매디슨 (Madison)',
 '캘리포니아주': '새크라멘토  (Sacramento)',
 '미네소타주': '세인트폴 (Saint Paul)',
 '오리건주': '세일럼 (Salem)',
 '캔자스주': '토피카 (Topeka)',
 '웨스트버지니아주': '찰스턴 (Charleston)',
 '네바다주': '카슨시티 (Carson City)',
 '네브래스카주': '링컨 (Lincoln)',
 '콜로라도주': '덴버  (Denver)',
 '노스다코타주': '비즈마크 (Bismarck)',
 '사우스다코타주': '피어 (Pierre)',
 '몬태나주': '헬레나 (Helena)',
 '워싱턴주': '올림피아 (Olympia)',
 '아이다호주': '보이시 (Boise)',
 '와이오밍주': '샤이엔 (Cheyenne)',
 '유타주': '솔트레이크시티 (Salt Lake City)',
 '오클라호마주': '오클라호마시티 (Oklahoma City)',
 '뉴멕시코주': '샌타페이 (Santa Fe)',
 '애리조나주': '피닉스 (Phoenix)',
 '알래스카주': '주노 (Juneau)',
 '하와이주': '호놀룰루  (Honolulu)'}

## 문제파일 만들고 순서 바꾸기

import random

# 35개 문제지 파일 만들기
for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # 문제지 헤더 작성하기
    quizFile.write('이름 : \t\t\t\t날짜 : \t\t\t\t학년 반 : \n\n')
    quizFile.write(('   ' * 20) + '미국 연방 주(state)의 수도 문제풀기 (유형 %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # 미국 주의 순서 섞기
    nations = list(capitals.keys())
    random.shuffle(nations)

    # 50개의 주를 반복하여 각각의 문제 만들기
    for questionNum in range(50):

        # 정답과 오답 만들기
        correctAnswer = capitals[nations[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOption = wrongAnswer + [correctAnswer]
        random.shuffle(answerOption)

        # 문제파일에 문제와 선택답안 쓰기
        quizFile.write('%s. %s의 수도는 무엇입니까?\n' % (questionNum + 1, nations[questionNum]))
        for i in range(4):
            quizFile.write('      %s. %s\n' % ('ㄱㄴㄷㄹ'[i], answerOption[i]))
        quizFile.write('\n')

        # 파일에 문제의 답 기록하기
        answerFile.write('%s. %s\n' % (questionNum + 1, 'ㄱㄴㄷㄹ'[answerOption.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
