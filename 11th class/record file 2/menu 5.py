print("Accept a list and a number and perform a linear search.\n Accept a list and sort in ascending order.\n Accept a list and delete a given element from the list.")
ch=int(input("enter choice "))
if ch==1:
    x=eval(input("enter list "))
    y=int("input number")
    for i in x:
        if 1==y:
            print("entered number was found")
            break
        else:
            print("entered number wasnt found")
if ch==2:
    x=eval(input("enter list "))
    print(x.sort())
if ch==3:
    x=eval(input("enter list "))
    y=int(input("enter element to be removed "))
    print(x.remove(y))
