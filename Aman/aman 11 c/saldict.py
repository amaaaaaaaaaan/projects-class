employee=dict()
i=1
n=int(input("enter no of entries"))
while i<=n:
    name=input("enter name")
    basic=int(input("enter basic salary"))
    hra=int(input("enter house rent allowance"))
    ca=int(input("enter convenance allowances"))
    sum=basic+hra+ca
    employee[name]=sum
    i=i+1
val=employee.keys()
print("\n name","\t\t","net salary")
for i in val:
    salary=0
    z=employee[i]
for j in z:
    salary=salary+j
    print(i,"\t\t",salary)
    