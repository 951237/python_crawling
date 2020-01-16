#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# 기본 이메일 보내기 스크립트
# 이메일 보내기 기본틀로 사용
'''

import smtplib, sys
smtpobj = smtplib.SMTP('smtp.gmail.com', 587) #구글계정 개체 생성
smtpobj.ehlo()
smtpobj.starttls()

email =  '951237@gmail.com'
smtpobj.login(email, sys.argv[1])       #스크립트

body = 'Subject : Mission Complete. \nTask is done.'

print('Sending email to %s. . . . ' % email)
sendmailStatus = smtpobj.sendmail(email, email, body) #처음 이멜은 발송 이메일, 두번째 이멜은 수신자 이멜 세번재 바디는 내용

print('Sending email to %s. . . . ' % email)

smtpobj.quit()