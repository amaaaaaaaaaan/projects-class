import mysql.connector as ms 
db=ms.connect(host="localhost",user="root",password="12345",database="faculty")
cu=db.cursor()

def f1():
    dt=input("Enter department name: ")
    cu.execute(f"select count(deptid) from teacher natural join posting where department='{dt}'")
    x=cu.fetchall()
    print(x)

def f2():
    tid=int(input("Enter teacher id: "))
    sl=int(input("Enter salary: "))
    cu.execute(f"update teacher set salary={sl} where tid={tid}")
    db.commit()

def f3():
    m1=int(input("Enter lower limit: "))
    m2=int(input("Enter upper limit: "))
    cu.execute(f"select name from teacher where salary>={m1} and salary<={m2}")
    x=cu.fetchall()
    for i in x:
        print(i)
while True:
    print('''
    1• Display number of teachers in a Department as per user input.
    2• Update Teacher’s Salary (Search by Tid)
    3• Display names of teachers within a range given by user.''')
    ch=int(input("Enter choice: "))

    if ch==1:
        f1()
    elif ch==2:
        f2()
    elif ch==3:
        f3()
    else:
        print("Invalid choice")
        break


