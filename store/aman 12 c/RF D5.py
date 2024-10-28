import pickle
import os
def app():
    with open ('EMPLOYEES.dat','ab')as f:
        while True:
            a=input('EMP NO      :')#string
            b=input('NAME        :')
            c=input('DESIGNATION :')
            d=int(input('SALARY  :'))
            rec=[a,b,c,d] # Create List
            pickle.dump(rec,f)# Write/Dump to file
            ch=input('Do you want to add more records ? ')
            if ch not in 'yY':
                break
        
def disp():
    f=open('EMPLOYEES.dat','rb')
    try:
        while True:
            data=pickle.load(f)
            print(data)
    except EOFError:
        print('--------------') 

def dispeno():
    with open('EMPLOYEES.dat','rb') as f:
        e=input('enter Eno:')
        found = False
        try:
            while True:
                l=pickle.load(f)
                if l[0]==e:
                    print(l)
                    found = True
        except EOFError:
            if found == False:
                print('Invalid Employee No')
            
def update():
    with open('EMPLOYEES.dat','rb') as f:
        newf=open('new.dat','wb')
        e=input('enter Eno:')
        found = False
        
        try:
            while True:
                l=pickle.load(f)
                
                if l[0]==e:
                    l[3]=int(input('Revised Salary : '))
                    found = True
                pickle.dump(l,newf)#Write records to new file
        except EOFError:
            if found == False:
                print('Invalid Employee No')
        newf.close()
    os.remove('EMPLOYEES.dat')
    os.rename('new.dat','EMPLOYEES.dat')

def delrec():
    with open('EMPLOYEES.dat','rb') as f:
        with open ('new.dat','wb')as newf:
            e=input('Enter Eno to be removed : ')
            found = False

            try:
                while True:
                    l=pickle.load(f)
                    if l[0]==e:
                        found = True
                    else:
                        pickle.dump(l,newf)
            except EOFError:
                if found == False:
                    print('Invalid Employee No')
    #Delete old file , Rename new file    
    os.remove('EMPLOYEES.dat')
    os.rename('new.dat','EMPLOYEES.dat')
    print('Successfully removed Employee No ',e)
   
while True:
    print('''\n------- MENU ---------
1. Append Records
2. Display Records
3. Search by Employee No
4. Update Salary of Employee
5. Delete Employee
0: Exit
''')
    i=int(input('Enter your choice : '))
    if i==1:
        app()
    elif i==2:
        disp()
    elif i==3:
        dispeno()
    elif i==4:
        update()
    elif i==5:
        delrec()
    elif i==0:
        exit()
    else:
        print('Please enter a valid value')