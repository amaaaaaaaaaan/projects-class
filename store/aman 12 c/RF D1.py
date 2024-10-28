def countdot():
    with open('poem.txt') as f:
        d1=f.read()
        return d1.count('.')
  
def wordI():
    with open('poem.txt') as f:
        data = f.read()
        countI=0
        word=data.split()
        return word.count('I')
        
def linesT():
    with open('poem.txt') as f:
        data=f.readlines()
        for i in data:
            if i[0] in 'tT':
                print(i,end='')
                
def firstlast():
    with open('poem.txt') as f:
        data=f.readlines()
        print('First Line : ', data[0],end='')
        print('Last Line : ', data[-1])

def longline():
    with open('poem.txt') as f:
        data=f.readlines()
        long=max(data,key=len)
        print('Longest line : ', long)
                
while True:
    print('\n=====      MENU       =====')
    print('''1. Count no of dots '.'
2. Count word ‘I’
3. Display lines starting with ‘tT’
4. Display the firts & last line 
5. Display the longest line
0. Exit
=======================================''')
    
    ch=int(input('Enter your choice : '))
    if ch==1:
        print('No of times "."  appears = ', countdot())
    elif ch==2:
        print('No of times word "I" appears = ',wordI())
    elif ch==3:
        linesT()
    elif ch==4:
        firstlast()
    elif ch==5:
        longline()
    elif ch==0:
        exit() 
    else:
        print('Wrong choice')