num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num2>num1:
    if num2>num3:
        print("2nd number is greatest")
elif num1>num3:
    if num1>num2:
        print("1st number is greater ")
elif num3>num1:
    if num3>num2:
        print("1st number is greater")
