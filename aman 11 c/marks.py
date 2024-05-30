lst1=[]
lst2=[]
for i in range(5):
    student=input("enter name")
    lst1.append(student)
    mark=input("enter mark")
    lst2.append(mark)
    high=max(lst2)
    low=min(lst2)
    highest=lst2.index(high)
    lowest=lst2.index(low)
print(lst1[highest],"got the highest marks")
print(lst1[lowest],"got the lowest marks")
