import mysql.connector as ms 
db=ms.connect(host="localhost",user="root",password="12345",database="ASSIGNMENT")
cu=db.cursor()
def add():
    r=int(input("enter roll no.: "))
    n=input("enter name: ")
    p=input("enter percentage: ")
    s=input("enter section: ")
    a=input("enter status of assignment: ")
    cu.execute(f"insert into student values({r},'{n}',{p},'{s}','{a}')")
    db.commit()

def display_status():
    a=input("enter status of assignment (PEDNING/SUBMITTED/EVALUATED): ")
    cu.execute(f"select * from student where assignment='{a}'")
    x=cu.fetchall()
    for i in x:
        print(i)

def rn_up():
    r=int(input("enter roll no of student: "))
    s=input("enter status of assignment: ")
    cu.execute(f"update student set assignment='{s}' where rollno={r}")
    db.commit()

def rn_del():
    r=int(input("enter roll no of student: "))
    cu.execute(f"delete from student where rollno={r}")
    db.commit()

def display():
    cu.excecute('select * from student')
    x=cu.fetchall()
    for i in x:
        print(i)
while True:
    print('''
    1. ADD New Records
    2. DISPLAY BY Status of Assignment
    3. Search by Roll No and UPDATE Status of Assignment
    4. Search by Roll No and DELETE Student Record
    5. DISPLAY ALL Records''')
    ch=int(input("Enter choice: "))

    if ch==1:
        add()
    elif ch==2:
        display_status()
    elif ch==3:
        rn_up()
    elif ch==4:
        rn_del()
    elif ch==5:
        display()
    else:
        print("Invalid choice")
        break





