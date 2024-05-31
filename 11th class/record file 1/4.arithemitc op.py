x=int(input("enter first number"))
y=int(input("enter second number"))
op=input("enter operator [+ , - , * , /] :")
if op=="+":
    print("Sum of numbers is :", x+y)
elif op=="-":
    print("Difference of numbers is :",x-y)
elif op=="*":
    print("product of numbers is :", x*y)
elif op=="/":
    print("quotient of numbers is :", x/y)
else:
    print("invalid operator")
