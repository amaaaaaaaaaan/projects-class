import pickle
import os
# Append records to the file.
# Display all records from the file.
# Display details of an employee.
f=open('Employee.dat','ab')
def app():
    rno=int(input("Enter roll no: "))
    rna=input("Enter student name: ")
    mar=int(input("Enter Marks: "))
    l=(rno,rna,mar)
    pickle.dump(l,f)

def dis():
    with open('Employee.dat','rb') as f:
        print("------------------")
        try:
            while True:
                a=pickle.load(f)
                print(a)
        except EOFError:
            print("-----------------")

def scor():
    with open('Employee.dat','rb') as f:
        try:
            while True:
                a=pickle.load(f)
                if a[2]>75:
                    print(a)
        except EOFError:
            print("-----------------")

def edi():
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