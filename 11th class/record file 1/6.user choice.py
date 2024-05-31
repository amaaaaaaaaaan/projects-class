a=int(input("Enter the number:"))
print("choose an option")
ch=int(input("1)check wether number is odd or even\n2)check if number is palindrome\n3)check wether if it is an Armstrong number\n---"))
if ch==1:
    if (a%2==0):
        print("The number is even.")
    else:
        print("The number is odd.")
elif ch==2:
    b=a
    reverse=0
    while b>0:
            remainder=b%10
            reverse=(reverse*10)+remainder
            b=b//10
    if a==reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")
elif ch==3:
    sum=0
    temp=a
    while temp>0:
        b=temp % 10
        sum+=b**3
        temp//=10
    if (a==sum):
        print(a,"is an Armstrong number")
    else:
        print(a,"is not an Armstrong number.")
else:
    print("Invalid option")
