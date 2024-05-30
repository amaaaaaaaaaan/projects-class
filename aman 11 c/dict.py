rec={}
n=int(input("enter number of employees"))
i=1
while i<=n:
    name=input("enter name")
    mark=int(input("enter mark"))
    rec[name]=mark
    i=i+1
print("name of student:\n" "% of marks:")
for i in rec:
    print(i,rec[i])
