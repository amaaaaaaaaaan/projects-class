import time

def pushelem():
    itmno=int(input("Enter emp No. :"))
    itmnm=input("Enter emp Name :")
    itnmpr=input("Enter dept :")
    stk.append({itmno:[itmnm,itnmpr]})

def popelem():
    if stk!=[]:
        print("Deleted employee is",stk.pop())
    else:
        print("Stack is Empty")

def displelem():
    if stk!=[]:
        for i in stk[::-1]:
            print(f'the stack is {i}')
    else:
        print("Stack is Empty")

stk=[]

for i in range (int(input(': '))):
    print("""
1.Push
2.Pop
3.Display
press any other key to exit
""")
    dtinp=int(input("Enter choice:"))
    if dtinp==1:
        pushelem()
    elif dtinp==2:
        popelem()
    elif dtinp==3:
        displelem()
    else:
        print("Program will be exited in ")
        exit()