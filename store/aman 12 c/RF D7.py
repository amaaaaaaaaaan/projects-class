import pickle
import os
'''Append records to the file.
• Display all records from the file
• Display details of students scoring > 75.
• Edit Name OR Mark of a Student (according to user’s choice)
• Search by RollNo and delete student details'''

f=open('Student.dat','ab')
def app():
    rno=int(input("Enter roll no: "))
    rna=input("Enter student name: ")
    mar=int(input("Enter Marks: "))
    l=(rno,rna,mar)
    pickle.dump(l,f)

def dis():
    with open('Student.dat','rb') as f:
        print("------------------")
        try:
            while True:
                a=pickle.load(f)
                print(a)
        except EOFError:
            print("-----------------")

def scor():
    with open('Student.dat','rb') as f:
        try:
            while True:
                a=pickle.load(f)
                if a[2]>75:
                    print(a)
        except EOFError:
            print("-----------------")

def edi():
    f=open("Student.dat",'rb')
    ch=input("Do u want to edit name or mark? ")
    if ch.lower()=='name':
        n=input("Enter name of student: ")
        try:
            while True:
                a=pickle.load(f)
                if a[1]==n.lower():
                    print(a)
        except EOFError:
            print("-----------------")

def update(ch):
    with open ('STUDENTS.dat','rb') as f:
        newf=open('newfile.dat','wb')
        r = int(input('Enter Roll No : '))
        found = False
        try:
            while True:
                data = pickle.load(f)#tuple
                if data[0] == r:
                    found = True
                    L=list(data)
                    if ch==1: # Edit name
                        L[1] = input('Enter new name : ')
                    else:# Edit mark
                        L[2] = int(input('Enter new mark : '))
                    data=tuple(L)
                pickle.dump(data,newf)
        except EOFError:
            if found == False:
                print('Enter a valid Roll No')
    newf.close()
    os.remove('STUDENTS.dat')
    os.rename('newfile.dat','STUDENTS.dat')
        

def delrec():
    with open ('STUDENTS.dat','rb') as f:
        newf=open('newfile.dat','wb')
        r = int(input('Enter Roll No : '))
        found = False
        try:
            while True:
                data = pickle.load(f)#tuple
                if data[0] == r:
                    found = True
                else:
                    pickle.dump(data,newf)
        except EOFError:
            if found == False:
                print('Enter a valid Roll No')
        newf.close()
    os.remove('STUDENTS.dat')
    os.rename('newfile.dat','STUDENTS.dat')

while True:
    print('''\n--------MENU--------
1. Append Records
2. Display Records
3. Display Student Details with score > 75
4. Update Name OR Mark of Student 
5. Delete a student record
0. Exit''')
    i = int(input('Enter your choice : '))
    if i == 1:
        app()
    elif i == 2:
        dis()
    elif i == 3:
        scor()
    elif i ==4:
        ch=int(input('Enter 1 to Edit Name OR 2 to Edit Mark : '))
        update(ch)
    elif i==5:
        delrec()
    elif i == 0:
        exit()
    else :
        print('Wrong choice ')