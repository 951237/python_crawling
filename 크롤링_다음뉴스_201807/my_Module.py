def emailMe():
    import smtplib
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587) #구글계정 개체 생성
    smtpobj.ehlo()
    smtpobj.starttls()

    email =  '951237@gmail.com'
    pw = input('Enter your Gmail password : ')
    smtpobj.login(email, pw)       #스크립트

    body = 'Subject : Mission Complete. \nTask is done.'

    print('Sending email to %s. . . . ' % email)
    sendmailStatus = smtpobj.sendmail(email, email, body) #처음 이멜은 발송 이메일, 두번째 이멜은 수신자 이멜 세번재 바디는 내용

    print('Done')

    smtpobj.quit()

def runSelenium():
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time

    url = input('Enter URL : ')

    driver = webdriver.Chrome()
    print('사이트에 접속중..')
    driver.get(url)
    driver.forward()
    time.sleep(0.25)
    return driver

# 함수 - bs4로 html 가져오기
def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    return bs_obj


if __name__ == '__main__':
    emailMe()