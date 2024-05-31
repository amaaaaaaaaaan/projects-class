print("1.Accept a list of numbers from the user and calculate the sum of it.\n Accept a list of numbers from the user and display even and odd elements in two different lists\nAccept a list from the user and find the largest and smallest number in alist ")
ch=int(input("Enter choice "))
if ch==1:
    x=eval(input("enter list "))
    print(x.sum())
elif ch==2:
    odd=[]
    even=[]
    x=eval(input("enter list "))
    for i in x:
        if i%2==0:
            odd.append(i)
        else:
            even.append(i)
    print("odd elements are: ", odd)
    print("even elements are: ",even)
elif ch==3:
    x=eval(input("enter list"))
    print("largest element is: ", x.max())
    print("smallest element is: ", x.min())
