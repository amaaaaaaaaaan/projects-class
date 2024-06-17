import statistics as st
while True:
    l=eval(input("enter list: "))
    print('''
1.Find Mean
2.Find Median
3.Find Mode''')
    ch=int(input("Enter choice"))
    if ch==1:
        mn=st.mean(l)
        print("Mean of list is: ",mn)
    elif ch==2:
        md=st.median(l)
        print("Median of listis: ",md)
    elif ch==3:
        mo=st.mode(l)
        print("Mode of list is: ",mo)