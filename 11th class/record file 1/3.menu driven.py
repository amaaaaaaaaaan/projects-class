x=int(input("select an option: \n 1)Area of a circle\n 2)Area of Rectangle\n 3)Circumference of Circle\n 4)Area of Square\n --"))
if x==1:
    r=int(input("Enter radius"))
    ar=3.14*r**2
    print("Area of circle is :",ar)
elif x==2:
    l=int(input("Enter length"))
    b=int(input("Enter breadth"))
    ar=l*b
    print("area of rectangle is :",ar)
elif x==3:
    r=int(input("enter radius"))
    cir=2*3.14*r
    print("circumfrence of circle is:",cir)
elif x==4:
    s=int(input("enter side"))
    ar=s**2
    print("Area of square is:", ar)
else:
    print("invalid option")