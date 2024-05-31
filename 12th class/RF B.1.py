def fib():
    n=int(input("enter the limit: "))
    x=0
    y=1
    z=1
    while z<=n:
        print(z,end=' ')
        print()
        x=y
        y=z
        z=x+y

def fact():
    n=int(input("enter the number: "))
    f=1
    for i in range(n,0,-1):
        f = f * i
    print(f"factorial of {n} is {f}")

def pr():
    n=int(input("enter value for n: "))
    count=0
    i=2 
    while count<n:
        for j in range(2,i):
            if i%j==0:
                break
        else: 
            print(i,end=' ')
            count+=1
        i+=1 
while True:
    print('''	    	
        1.	Find factorial of a number, n!
        2.	Print first n Prime numbers.
        3.	Display Fibonacci Series up to count ‘n’.
    ''')
    ch=int(input("enter choice: "))
    if ch==1:
        fact()
    elif ch==2:
        pr()
    elif ch==3:
        fib()
    else:
        print("Invalid choice")
        break