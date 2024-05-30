# RECORD FILE - B.1 INTEGER
'''Design a Python program that accepts a number 'n'.
   And gives the user options to :  	    	
    1.	Find factorial of a number, n!
    2.	Print first n Prime numbers.
    3.	Display Fibonacci Series up to count ‘n’.
'''
import time
def factorial(n):
    f=1
    for i in range(n,0,-1):
        f = f * i
    print(n,"! = ", f)
    
def prime(n): # first n prime numbers
    count=0
    i=2  # First prime no
    while count<n:
        for j in range(2,i):
            if i%j==0:
                break
        else: 
            print(i,end=' ')
            count+=1
        i+=1 # check if each no is prime till count = n
        
def fibonacci(n):
    First,Second = 0 , 1
    for i in range(n):
        print(First, end=" ")
        Third = First + Second
        First,Second = Second, Third
    print('\n')

#Main
ch = 'Y'
n = int(input('Enter the number : '))
while ch in 'Yy':
    print('\n----- MENU -----')
    print('1. Factorial \n2.Prime \n3.Fibonacci \n0.Exit')
    op = int(input('Enter your choice : '))
    print()
    if op == 1:
        factorial(n)
    elif op == 2:
        print('First ' , n ,' Prime numbers : ', end ='')
        prime(n)
    elif op == 3:
        print('Fibonnaci Series : ',end ='')
        fibonacci(n)
    elif op ==0:
        print('Exiting.....')
        time.sleep(3)
        exit()
    else:
        print('Wrong Choice. Enter correct Option.')
        
    
    
