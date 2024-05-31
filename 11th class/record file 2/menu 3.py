print(" 1.Accept a string print it in lowercase\n 2.Accept a string print it in uppercase\n 3.Accept a string and count the number of alphabets, digits andspecial characters in a string.")
ch=int(input("Enter choice "))
if ch==1:
    x=input("enter string ")
    print(x.lower())
if ch==2:
    x=input("enter string")
    print(x.upper())
if ch==3:
    alpha=0
    dig=0
    spl=0
    x=input("enter string")
    for i in x:
        if i.isalpha():
         alpha=alpha+1
        elif i.isdigit():
            dig=dig+1
        else:
            spl=spl+1
    print("number of alphabets is: ", alpha)
    print("number of digits is: ", dig)
    print("number of special charecters is: ", spl)
    

    