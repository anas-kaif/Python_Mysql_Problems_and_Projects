# import pymysql
# conn=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="manuu123",
#     database="manuu"
# )
# cursor=conn.cursor()
# # query="CREATE TABLE staff (id INT PRIMARY KEY, salary DECIMAl(10,2) NOT NULL);"
# # query="""INSERT INTO staff(id,salary) VALUES
# # (1,5000.45),
# # (3,34090.45);"""
# # cursor.execute(query)
# # conn.commit()

# #print("next line\n",cursor.fetchall())
# #print(rows)
# # conn.commit()
# cursor.execute("SELECT id FROM staff")
# rows=cursor.fetchall()
# # print(rows)
# for row in rows:
#     print(row)
# conn.close()
import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="manuu123",
    database="manuu"

)
cursor =conn.cursor()
query="DROP TABLE student;"
cursor.execute(query)
query="SHOW TABLES;"
cursor.execute(query)
for el in cursor.fetchall():
    print(el)

conn.close()