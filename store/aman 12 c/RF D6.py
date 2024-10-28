import pickle
import os
def append():
    if os.path.isfile('book.dat'): # If file exists
        print('File exists , continuing will erase data')
    else:
        with open('book.dat', 'wb') as f:
            data={}
            while True:
                bno=input('BOOK NO   : ')
                name=input('BOOK NAME : ')
                price=float(input('PRICE    : '))
                data[bno]=[name,price] #Create dictionary
                ch=input('Do you want to add more records Y/N ?')
                if ch not in 'yY':
                    break
            pickle.dump(data,f)
            print('   Data entered    ')
            
def displayall():
    if os.path.isfile('book.dat'): # If file exists
        with open('book.dat', 'rb') as f:
            print('BOOK NO \t TITLE OF BOOK \t\t PRICE')
            try:
                while True:
                    data=pickle.load(f)
                    k=data.keys() # get keys of dictionary
                    for i in k:
                        print(i,'\t\t',end ='') # key
                        print(data[i][0],'\t\t',data[i][1])
                        
            except EOFError:
                print('-'*20)
    else:
        print('File does not exist')

def searchbook(bno):
    if not os.path.isfile('book.dat'): # If file exists
        print('File does not exist')
    else:
        with open('book.dat', 'rb') as f:
            print('BOOK NO \t TITLE OF BOOK \t\t PRICE')
            try:
                while True:
                    data=pickle.load(f)
                    k=data.keys() # get keys of dictionary
                    if bno not in k:
                        print('Invalid Book No ')
                        break
                    else:
                        print(bno,'\t\t',end ='') # key
                        for j in data[bno]:
                            print(j,'\t\t\t',end='')
                        print()      
            except EOFError:
                print('-'*50)
    
        
def updateprice(bno):
    if not os.path.isfile('book.dat'):
        print('File does not exist')
    else:
        with open('book.dat','rb') as f:
            try:
                while True:
                    data=pickle.load(f)
                    k=data.keys() 
                    if bno not in k:
                        print('Invalid Book No !!!  ')
                        break
                    else: 
                        newp=float(input('Enter new price'))
                        data[bno][1]=newp
                        break
            except EOFError:
                print('-'*20,'End of File','-'*20)
                
        with open('book.dat','wb') as f1:
                pickle.dump(data,f1)
        del data
        
while True:
    print('''\n------- MENU ---------
1. Create File & Append Records
2. Display all Records
3. Search by Book No and display details
4. Search by Book No and update Price
0: Exit
''')
    i=int(input('Enter your choice : '))
    if i==1:
        append()
    elif i==2:
        displayall()
    elif i==3:
        print('=== CHECK FOR BOOK ===')
        bno=input('BOOK NO: ')
        searchbook(bno)
    elif i==4:
        bno=input('BOOK NO : ')
        updateprice(bno)
    elif i==0:
        exit()
    else:
        print('Please choose a valid option')

