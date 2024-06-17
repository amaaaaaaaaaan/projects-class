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

while True:
    print('''
1.ACCEPT new employee details and display all records. 
2.DISPLAY employee details by employee number; display appropriate message if employee number not matched. 
3.UPDATE the Salary by employee number.  
4.DELETE Record by employee number.
''')
    ch=int(input("Enter choice: "))
    if ch==1:
        f1()
    elif ch==2:
        f2()
    elif ch==3:
        f3()
    elif ch==4:
        f4()
    else:
        print("Invalid choice")
        break


