student=dict()
i=1
n=int(input("enter no. of students "))
while i<=n:
    adn=input("enter admission number ")
    name=input("enter name ")
    section=input("enter section ")
    per=float(input("enter percentage "))
    b=(name,section,per)
    student[adn]=b
    i+=1
val=student.keys()
for i in val:
    print("adno", i,":")
    z=student[i]
    print("name","section","percentage") 
    for j in z:
        print(j)
