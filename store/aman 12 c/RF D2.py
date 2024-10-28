def entercity():
    with open('Cities.txt','a+') as f:
        ch ='y'
        while ch in 'Yy':
            data = input('Enter City : ')
            f.write(data + '\n')
            ch=input('Do you want to enter City name (y/n) ?')
def display():
    with open('Cities.txt','r') as f:
        print()
        print(f.read(),end='')

def vccount():
    with open('Cities.txt','r') as f:
        print()
        v,c=0,0
        data=f.read()
        for i in data:
            if i.isalpha():
                if i.lower() in 'aeiou':
                    v+=1
                else:
                    c+=1
        print('No of Vowels =',v, '\nNo of Consonants =',c)

def createACity():
    with open('ACities.txt','w+') as f2:
        with open('Cities.txt','r') as f1:
            L = f1.readlines()
            for i in L:
                if i[0] in 'Aa':
                    f2.write(i) # Writing to file ACities
            f2.seek(0)
            print('New File \n', f2.read())

def replacei():
    with open("Cities.txt","r+") as f:
        s=f.read()
        s=s.replace('i','!')
        s=s.replace('I','!')
        f.seek(0)
        f.truncate()
        f.write(s)
        print('\nEDITED TEXT CONTENTS\n',f.read())
        
                    
while True:
    print('\n===== MENU =====')
    print('''
1. Enter City names
2. Print File contents
3. No of vowels & consonants
4. Create file ACities
5. Replace 'i' with '!'.
0. Exit
===================''')

    ch=int(input('Enter your choice : '))
    if ch==1:
        entercity()
    elif ch==2:
        display()
    elif ch==3:
        vccount()
    elif ch==4:
        createACity()
    elif ch==5:
        replacei()
    elif ch==0:
        break
    else:
        print('Wrong choice')
