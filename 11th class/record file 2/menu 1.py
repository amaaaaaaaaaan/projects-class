print(" 1.check whether the string is a palindrome or not.\n 2.check whether the entered strings are equal or not.\n 3.return a string having first letter of each wordin capital letter.")
ch=int(input("Enter choice "))
if ch==1:
    num=int(input("enter number "))
    p=num
    rev=0
    while p>0:
        pn=p%10
        rev=(rev*10)+pn
        p=p//10
    if rev==num:
        print("palindrome")
    else:
        print("not a palindrome")
elif ch==2:
    x=input("enter first string ")
    y=input("enter second string ")
    if x==y:
        print("the strings are equal")
    else:
        print("strings arent equal")
elif ch==3:
    x=input("enter string ")
    print(x.title())
    
    
