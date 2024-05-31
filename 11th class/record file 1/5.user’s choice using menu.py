while True:
    print("1.Multiplication table\n")
    print("2.Fibonacci\n")
    print("3.factorial\n")
    ch=int(input("enter your choice:enter 0 to exit"))
    if ch==1:
        x=int(input("enter the no for which table is required"))
        i=1
        while(i<=10):
            print(x,"X",i,"=",x*i)
            i+=1
    elif ch==2:
        i=int(input("enter the limit"))
        x=0
        y=1
        z=1
        print("\nFibonacci\n")
        print(x)
        print(y)
        while z<=i:
            print(z,end=' ')
            print()
            x=y
            y=z
            z=x+y
    elif ch==3:
        n=int(input("Enter number:"))
        fact=1
        while(n>0):
            fact=fact*n
            n=n-1
        print("Factorial of the number is: ")
        print(fact)
    elif ch==0:
        break
    else:
        print("invalid")
        