import statistics as st
l=eval(input("enter list: "))
while True:
    print('''
1.Find Mean
2.Find Median
3.Find Mode''')
    ch=int(input("Enter choice: "))
    if ch==1:
        mn=st.mean(l)
        print("Mean of list is: ",mn)
    elif ch==2:
        md=st.median(l)
        print("Median of listis: ",md)
    elif ch==3:
        mo=st.mode(l)
        print("Mode of list is: ",mo)