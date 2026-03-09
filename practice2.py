import os
from dotenv import load_dotenv
import pymysql

load_dotenv()
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_host"),
        user=os.getenv("DB_user"),
        database=os.getenv("DB_database"),
        password=os.getenv("DB_password")
    )

conn=get_db_connection()
#Default cursor feching data from DB as tuple
cursor=conn.cursor()
cursor.execute("SELECT *FROM student;")
data=cursor.fetchall()
# for row in data:
#     print(row)
print(data[0][0])        #show 1st row 1st column data only
print(data[0][1])        #show 1st row 2nd column data 
cursor.close()
conn.close()

