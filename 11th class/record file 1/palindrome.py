num=int(input("enter number"))
p=num
rev=0
while p>0:
    pn=p%10
    rev=(rev*10)+pn
    p=p//10
if rev==num:
    print("palindrome")
    


    
    
    