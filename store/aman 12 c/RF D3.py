import csv

def append():
    with open ("payroll.csv", "a",newline="") as f:
        csvW=csv.writer(f)
        data =[int(input("Employee No\t: ")),input("Name\t: "),int(input("Salary\t: "))]
        csvW.writerow(data)  

def display():
    with open("payroll.csv", "r") as f: 
        csvR = csv.reader(f)
        for r in csvR:print(r[0],'\t',r[1],'\t\t',r[2])
    print('-' * 25)

def search():
    with open("payroll.csv", "r") as f: 
        csvR = csv.reader(f)        
        next(csvR)                   
        for r in csvR:              
            if int(r[2])>=10000:print(r[0],'\t',r[1],'\t\t',r[2])

while True:
    ch=int(input('''\n------- MENU ---------
1. Append Records
2. Display Records
3. Records with Salary greater than 10000
0: Exit
Enter your choice:'''))
    if ch==1:append()
    elif ch==2:display()
    elif ch==3:search()
    elif ch==0:break
    else:print('Invalid option')
    
        

