print("Accept a list of 5 student names and print it in alphabetical order.\nAccept a list of 5 students name and marks and print the name andmarks of student who got the highest and lowest marks.\n Accept a list and insert a value in a particular position of anexisting list.")
ch=int(input("enter choice "))
if ch==1:
    x=eval(input("enter names of 5 students as list "))
    print(x.sorted())
elif ch==2:
    names = []
    marks = []
    for i in range(5):
        name = input(f"Enter student name {i + 1}: ")
        mark = float(input(f"Enter marks for {name}: "))
        names.append(name)
        marks.append(mark)
    highest = marks.index(max(marks))
    lowest = marks.index(min(marks))
    print(f"The student with the highest marks is {names[highest]} with {marks[highest]} marks.")
    print(f"The student with the lowest marks is {names[lowest]} with {marks[lowest]} marks.")
elif ch==3:
    x=eval(input("enter list "))
    y=input("enter element")
    s=int(input("eneter position"))
    print(x.insert(s,y))
    
    