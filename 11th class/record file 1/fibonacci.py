i=int(input("enter the limit"))
x=0
y=1
z=1
while z<=i:
    print(z,end=' ')
    print()
    x=y
    y=z
    z=x+y
