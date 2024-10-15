import mysql.connector as ms
db=ms.connect(host="localhost",user="root",password="12345",database="company")
cu=db.cursor()

en=int(input("Enter empno: "))
nm=input("Enter name: ")
dt=input("Enter dept: ")
sy=int(input("Enter salary: "))
cu.execute(f"insert into employee values({en},'{nm}','{dt}',{sy})")
db.commit()
cu.execute("select * from employee")
x=cu.fetchall()
for i in x:
    print(i)
