import csv
import os

def checkfile():
    if not os.path.isfile('LOGIN.csv'): # Check if file exists
            with open ("LOGIN.csv", "w",newline="") as f:
                csvW=csv.writer(f) # CSV Writer Object
                fields = ['UNAME','PSWD'] # Heading
                csvW.writerow(fields)

def append():
    user = input("Username\t: ")
    chk=True
    #Checking if username exists
    with open('LOGIN.csv', "r+") as f: 
        csvR = csv.reader(f)
        next(csvR)   
        for r in csvR:
            if r[0].lower() == user.lower():
                print('Username exists')
                chk = False
                break
    if chk == True:
        with open('LOGIN.csv', "a+",newline="") as f:
            csvW=csv.writer(f)
            pswd = input("Password\t: ")
            data= [user,pswd]
            csvW.writerow(data)
        

def display():
    if not os.path.isfile('LOGIN.csv'):
        print('Check file name !!! File does not exist. ')
    else:
        with open('LOGIN.csv', "r") as f: 
            csvR = csv.reader(f)        # CSV Reader Object is created
            for r in csvR:# reads the file contents record by record
                print(r[0],'\t',r[1])
        print('-' * 25)

   
def searchPWD():
    with open('LOGIN.csv', "r") as f: 
        csvR = csv.reader(f)        # FileObj f is converted to reader object csvR  
        next(csvR)
        n = input('Enter Username : ')
        for r in csvR:          
            if r[0].lower() == n.lower():
                print('Password is : ', r[1])
        print("\nSearch over......")
#main
while True:
    print('''\n------- MENU ---------
1. Append Records
2. Display Records
3. Search and display password of user
0: Exit
''')
    i=int(input('Enter your choice : '))
    if i==1:
        checkfile() # Check if file exists
        append()
    elif i==2:
        display()
    elif i==3:
        searchPWD()
    elif i==0:
        exit()
    else:
        print('Please choose a valid option')