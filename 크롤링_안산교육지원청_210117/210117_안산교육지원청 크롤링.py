# 안산교육지원청 데이터를 크롤링해서 sql DB에 저장

import pandas as pd
import ssl
import sqlite3
from datetime import date
from tqdm import tqdm

ssl._create_default_https_context = ssl._create_unverified_context

PATH_DB = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_python/python_db/db_crawling.db"
DATE_TODAY = date.today().strftime('%y.%m.%d')

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

# 부서별 업무 내용 크롤링 feat 판다스
def get_ansan_office_info(p_key, p_val):
    # global date_create
    URL = f'https://www.goeas.kr/USR/ORG/MNU6/OrgDetail.do?orgType={p_val}'
    lst_df = pd.read_html(URL, header=0)
    df = pd.DataFrame()
    for i in lst_df:
        df = df.append(i)
    df['부서'] = p_key
    df['생성일'] = DATE_TODAY
    df = df[['부서','직위', '성명', '담당업무','생성일']]
    df.columns = ['department', 'position', '_name', '_charge', 'create_time']
    return df

def save_db(p_df):
    con = sqlite3.connect(PATH_DB)  #db에 접속
    p_df.to_sql('db_ansan_edu_office', con, index=False, index_label=False, if_exists='append')

print('Starting mission')
for k, v in tqdm(dic_url.items(), desc = 'DB생성'):
    df = get_ansan_office_info(k, v)
    save_db(df)
print('Mission Complete!')


# sql DB생성하기
# 데이터 프레임 DB저장하기 
# 기존 DB와 비교해서 내용이 바뀐 경우 업데이트 하기 / 비고란에 업데이트 날짜 기록하기

