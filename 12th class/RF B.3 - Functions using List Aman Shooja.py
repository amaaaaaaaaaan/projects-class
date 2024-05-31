def swp(n):
    s1=[]
    s2=[]
    l=int(len(n)/2)
    if len(n)%2==0:
        for i in n[0:l]:
            s1.append(i)
        for i in n[l:len(n)]:
            s2.append(i)
    print(s2+s1)

def ed(n):
    v=[]
    for i in n:
        if i%2==0:
            v.append(i//2)
        else:
            v.append(i*2)
    print(v)

def swed(n):
    l=len(n)
    for i in range(0,l,2):
        n[i],n[i+1]=n[i+1],n[i]
    print('After swap even & odd position) : ',n) 

def LScrl(n):
    l=len(n)
    temp=n[0]
    for i in range(0,l-1):
        n[i]=n[i+1]
    n[l-1]=temp
    print('After Left Scroll : ',n)

while True:
    print('''
    1.      Swap elements in even and odd position
    2.      Edit List - EvenNo/2 & OddNo*2
    3.      Left Scroll elements
    4.      Swap 1st half with 2nd half''')
    ch=int(input("Enter choice: "))
    if ch==1:
        x=eval(input("Enter list: "))
        swed(x)
    elif ch==2:
        x=eval(input("Enter list: "))
        ed(x)
    elif ch==3:
        x=eval(input("Enter list: "))
        LScrl(x)
    elif ch==4:
        x=eval(input("Enter list: "))
        swp(x)
    else:
        print("Invalid option")
        break
