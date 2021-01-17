import database

PATH_DB = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_python/python_db/db_crawling.db"

PARAM_DB_TABLE_MAIN = "db_ansan_edu_office"

db = database.SqliteDb()
db.connect(PATH_DB)

df = db.get_dataframe(PARAM_DB_TABLE_MAIN)

df.columns

def find_value(p_col, p_val):
    return df.loc[df[p_col] == p_val]

def find_incl_val(p_col, p_val):
    return df.loc[df[p_col].str.contains(p_val), :]

find_value('_name', '이동호')
find_incl_val('_charge', '발명')

