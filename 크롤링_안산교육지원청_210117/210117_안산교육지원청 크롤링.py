# 안산교육지원청 데이터를 크롤링해서 sql DB에 저장

import pandas as pd
import ssl
import sqlite3
from datetime import date
from tqdm import tqdm

# 크롤링 중 인증서 오류 해결 코드 
ssl._create_default_https_context = ssl._create_unverified_context

PATH_DB = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_python/python_db/db_crawling.db"    # 데이터베이스 경로
DATE_TODAY = date.today().strftime('%y.%m.%d')  # 오늘 날짜 

# 부서별 크롤링 위한 딕셔너리
dic_url = {
    '초등교육지원과': 'A',
    '중등교육지원과': 'B',
    '평생교육건강과': 'C',
    '경영지원과': 'D',
    '학교현장지원과': 'E',
    '교육시설과': 'F',
    '교육시설관리센터': 'G'
}


def make_id(df, p_val):
    '''
    - 인덱스 값을 초기화한 후에 인덱스 값을 이용해서 고유 id 만들기
    - return df
    '''
    df.reset_index(drop='index', inplace=True)
    df['id'] = df.index + 1
    df['id'] = df['id'].astype(str)
    df['id'] = p_val + df['id']
    return df

# 부서별 업무 내용 크롤링 feat 판다스
def get_ansan_office_info(p_key, p_val):
    '''
    - 판다스 read_html을 이용해서 안산교육지원청 부서별 업무 데이터 크롤링
    - 딕셔너리의 값을 이용해서 크롤링
    - return : df
    '''
    # global date_create
    URL = f'https://www.goeas.kr/USR/ORG/MNU6/OrgDetail.do?orgType={p_val}'
    lst_df = pd.read_html(URL, header=0)
    df = pd.DataFrame()
    for i in lst_df:
        df = df.append(i)
    df['부서'] = p_key
    df['생성일'] = DATE_TODAY
    df = make_id(df, p_val)
    df = df[['id', '부서','직위', '성명', '담당업무','생성일']]
    df.columns = ['id', 'department', 'position', '_name', '_charge', 'create_time']
    return df

# 테이블 데이터 모두 삭제
def delete_all_tasks(con):
    """
    Delete all rows in the tasks table
    :param con: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM ansan_edu_office'
    cur = con.cursor()
    cur.execute(sql)
    con.commit()

def save_db(con, p_df):
    '''
    - sql 데이터 베이스에 접속해서 데이터프레임을 저장하기
    - return : None
    '''
    p_df.to_sql('ansan_edu_office', con, index=False, index_label=False, if_exists='append')

def main():
    con = sqlite3.connect(PATH_DB)  # db에 접속
    delete_all_tasks(con)   # 기존데이터 삭제
    print('Starting mission')
    for k, v in tqdm(dic_url.items(), desc = 'DB생성'):
        df = get_ansan_office_info(k, v)
        save_db(con, df)
    print('Mission Complete!')

if __name__ == "__main__":
    main()



