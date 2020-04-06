from urllib import request
from bs4 import BeautifulSoup as soup


class Review:
    def __init__(self, comment, date, star, good, bad):
        self.comment = comment
        self.date = date
        self.star = star
        self.good = good
        self.bad = bad

    def show(self):
        print("내용 : " + self.comment +
              "\n날짜 : " + self.date +
              "\n별점 : " + self.star +
              "\n좋아요 : " + self.good +
              "\n싫어요 : " + self.bad)


<<<<<<< .merge_file_a19124
URL = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=134963'
=======
URL = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=189001'
>>>>>>> .merge_file_a16028


def get_html(url):
    html = request.urlopen(url)
    bs_obj = soup(html, "html.parser")
    print('페이지 소스 로딩 완료!\n')
    return bs_obj


def crawl(soup):
    review_list = []
    # title = soup.find('h3', {'class' : 'h_movie'}).find('a').text
    title = soup.find('h3', class_='h_movie').find('a').text  # 영화제목 추출
    div = soup.find('div', class_='score_result')

    data_list = div.select("ul > li")  # 평정 영역의 한줄평 선택

    for review in data_list:
        star = review.find('div',
                           class_='star_score').text.strip()  # strip() 빈공간 여백 삭제
        reply = review.find('div', class_='score_reple')  # 리뷰 선택하기
        comment = reply.find("p").text.strip()  # 리뷰 내용
        date = reply.select("dt > em")[1].text.strip()  # 리뷰 날짜
        button = review.find('div', class_='btn_area')  # 버튼 영역 선택
        sympathy = button.select("a > strong")  # 리뷰의 공감과 비공감 선택 태그 부분 선
        good = sympathy[0].text  # 좋아요 수치
        bad = sympathy[1].text  # 싫어요 수치
        review_list.append(Review(comment, date, star, good, bad))
    return title, review_list


soup = get_html(URL)
title, review_list = crawl(soup) #제목과 크롤링한 리뷰내용 리턴

print(f'제목 : {title}')
for review in review_list:
    review.show()
    print()
