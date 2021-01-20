import pandas as pd 
import sqlite3

'''
CREATE TABLE ansan_edu_office (
    id text primary key,
    department text not null,
    position text,
    _name text,
    _charge integer not null,
    create_time text not null
);
'''


# DB 위치
PATH_DB = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_python/python_db/db_crawling.db"
TABLE_NAME = 'ansan_edu_office'     # 테이블 이름

conn = sqlite3.connect(PATH_DB) 
cur = conn.cursor() 

def make_df_from_sql_all(p_cur):
    '''
    - 데이터베이스 전체 데이터 프레임 만들기
    - p_cur : sqlite 오브젝트
    '''
    sql = f"SELECT * FROM {TABLE_NAME}"
    p_cur.execute(sql) 
    rows = p_cur.fetchall() 
    cols = [column[0] for column in p_cur.description] 
    df = pd.DataFrame.from_records(data=rows, columns=cols)
    return df

def make_df_query_colname(p_col, p_keyword):
    '''
    - 칼럼이름으로 데이터 프레임 만들기
    - ex) make_df_from_sql_colname('department', "'초등교육지원과'") # 겹따옴표
    - p_cur : sqlite 오브젝트
    - p_col : DB 칼럼 명
    - p_keyword : 검색하고 싶은 키워드
    '''
    sql = f"SELECT * FROM {TABLE_NAME} WHERE {p_col} == {p_keyword}"
    df = pd.read_sql_query(sql, conn)
    return df

def make_df_query_like(p_col, p_keyword):
    '''
    - 칼럼에 단어가 포함된 레코드 찾기
    - ex) make_df_query_like('position', '장학사')
    - p_cur : sqlite 오브젝트
    - p_col : DB 칼럼 명
    - p_keyword : 검색하고 싶은 키워드
    '''
    sql = f"SELECT * FROM {TABLE_NAME} WHERE {p_col} LIKE '%{p_keyword}%'"
    df = pd.read_sql_query(sql, conn)
    return df

def make_list_from_sql(p_cur, p_col, p_keyword):
    '''
    - p_cur : sqlite 오브젝트
    - p_col : DB 칼럼 명
    - p_keyword : 검색하고 싶은 키워드
    '''
    sql = f"SELECT * FROM {TABLE_NAME} WHERE {p_col} LIKE '%{p_keyword}%'"
    lst = []
    p_cur.execute(sql) 
    rows = p_cur.fetchall() 
    for row in rows: 
        lst.append(row)
    return lst

def show_charge_split(lst):
    '''
    - lst : 업무내용이 포함된 것을 분리해서 이름과 함께 출력하기
    - lst[0] : id / lst[1] : 부서 / lst[2] : 직위 / lst[3] : 이름 / lst[4] : 업무내용
    '''
    for i, val in enumerate(lst):
        print(f'{i}. {val[3]}({val[1]})')     # val[3] : 
        if '•' in val[4]:
            for k in val[4].split('•')[1:]:
                print(f'# {k}')
            print("")
        elif '-' in val[4]:
            for k in val[4].split('-')[1:]:
                print(f'# {k}')
            print()
        else:
            print(val[4])
            print("")

def main():
    # 직책 검색해서 화면 출력하기
    # lst = make_list_from_sql(cur, 'position', '주무관')
    # show_charge_split(lst)
    df = make_df_from_sql_all(cur)
    print(df)

if __name__ == "__main__":
    main()
