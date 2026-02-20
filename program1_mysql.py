import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="manuu123",
    database="manuu"
)
cursor=conn.cursor()
query="SHOW TABLES;"
cursor.execute(query)
# for ele in cursor.fetchall():
#     print(ele)
print(cursor.fetchall())
query="SELECT * FROM scholar;"
cursor.execute(query)
for ele in cursor.fetchall():
    print(ele)

conn.close()