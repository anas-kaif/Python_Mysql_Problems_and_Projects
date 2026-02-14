import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="manuu123",
    database="manuu"
)
cursor=conn.cursor()
# query="CREATE TABLE scholar(roll VARCHAR(11) PRIMARY KEY," \
# "name VARCHAR(100) NOT NULL," \
# "gender ENUM('Male','Female','Other')," \
# "city VARCHAR(100));"
# #cursor.execute(query)
# #conn.commit()
# query="DESC scholar;"
# cursor.execute(query)
# for ele in cursor.fetchall():
#     print(ele)
def Add_student(roll,name,gender,city):
    query="INSERT INTO scholar VALUES(%s,%s,%s,%s);"
    cursor.execute(query,(roll,name,gender,city))
    print("Added successfully...")
    conn.commit()
def Delete_student(roll,name):
    query="DELETE FROM scholar WHERE roll=%s AND name=%s;"
    cursor.execute(query,(roll,name))
    conn.commit()
    print("Deleted Successfully...")

def Edit_student(roll,name,city):
    query="""UPDATE scholar
    SET name=%s,city=%s
    WHERE roll=%s"""
    cursor.execute(query,(name,city,roll))
    conn.commit()
    print("Updated Successfully..")
def Detaile_student(roll,name):
    query="""SELECT * FROM scholar WHERE roll=%s AND name=%s"""
    cursor.execute(query,(roll,name))
    data=cursor.fetchall()
    for ele in list(data):
        print(ele)
    conn.close()
    print("Details Successfully...")

ste="\t\t\thello,welcome to student management system"
str=ste.title()
print(str)
print("\n(1)Add Student\t(2)Update \n(3)Delete\t(4)Check Details")
choice=int(input("Enter Your Choice:"))
if choice==1:
    id=input("Enter Student Roll No.:")
    name=input("Enter Student Name:")
    gender=input("Enter Student Gender:")
    city=input("Enter Student Hometown:")
    Add_student(id,name,gender,city)
    conn.close()
elif choice==2:
    id=input("Enter Updating Student Roll No.:")
    name=input("Enter Student Correct Name:")
    city=input("Enter Student Correct Hmetown:")
    Edit_student(id,name,city)
elif choice==3:
    id=input("Enter Deleting Student Roll No.:")
    name=input("Enter Student Name:")
    Delete_student(id,name)
    conn.close()
elif choice==4:
    id=input("Enter Student Roll No.:")
    name=input("Enter Student Name:")
    Detaile_student(id,name)
