import time

def pushelem(stk,item):
    stk.append(item)

        
def dispelem(stk): 
    if stk !=():
        print('Empty stack')
    for i in stk[::-1]:
        print(f'the stack is {i}')

def popelem(stk):
    print("Deleted Item : ", stk.pop())
      


stk=()
for i in range (int(input(': '))):
    print('''
    1.Push element
    2.display element
    3.pop element
    press any other key to exit
   ''')
    ch=int(input("Enter your choice : "))
    print("\n")
    if ch==1:
        bk =input("Enter Book No :")
        bknm =input("Enter Book Name :")
        bkco=float(input("Enter Cost of book : "))
        bkdta=(bk,bknm,bkco)
        pushelem(stk,bkdta)
    elif ch==2:
        popelem(stk)
    elif ch==3:
        dispelem(stk)
    else:
        print("Exiting program........")
        time.sleep(3)
        exit()