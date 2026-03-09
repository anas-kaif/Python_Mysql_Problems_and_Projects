import os
import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv
load_dotenv()
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_host"),
        user=os.getenv("DB_user"),
        database=os.getenv("DB_database"),
        password=os.getenv("DB_password")
    )
conn=get_db_connection()
#fetching data from DB as a list
cursor=conn.cursor(DictCursor)
cursor.execute("SELECT *FROM student;")
data=cursor.fetchall()
print(type(data))
print(data[0]["NAME"])
cursor.close()
conn.close()