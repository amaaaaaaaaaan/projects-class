import mysql.connector as ms
db=ms.connect(host="localhost",user="root",password="12345",database="company")
cu=db.cursor()

def f1():
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

def f2():
    ch=int(input("Enter employee number: "))
    cu.execute(f"select * from employee where empno={ch}")
    x=cu.fetchall()
    if x==[]:
        print("Invalid employee number")
    else:
        print(x)

def f3():
    e=int(input("Enter employee number: "))
    s=int(input("Enter salary: "))
    cu.execute(f"update employee set salary={s} where empno={e}")
    db.commit()

def f4():
    e=int(input("Enter employee number: "))
    cu.execute(f"delete from employee where empno={e}")
    db.commit()
f4()
    
