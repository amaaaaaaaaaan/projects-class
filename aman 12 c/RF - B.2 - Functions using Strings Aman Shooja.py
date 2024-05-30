def vow(n):
    v=["a","e","i","o","u"]
    x=""
    for i in n:
        if i in v:
            continue
        else:
            x=x+i
    print(x)

def count(n):
    al=0
    nm=0
    sp=0
    sc=0
    for i in n:
        if i.isalpha():
            al=al+1
        elif i.isdigit():
            nm=nm+1
        elif i==" ":
            sc=sc+1
        else:
            sp=sp+1
            print(i)
    print("no.of charecters:",al,"\nno. of digits:",nm,"\nno. of special charecters:",sp,"\nno. of spaces:",sc)

def const(n):
    v=["a","e","i","o","u"]
    x=""
    for i in n:
        if i in v:
            x=x+i
        else:
            x=x+"*"
    print(x)

def pali(n):
    e=""
    for i in n[::-1]:
        e=e+i
    if e==n:
        print("String is palindrome")
    else:
        print("String is not palindrome")
 
while True:   
    print('''
        1. Check if palindrome
        2. Count number of alphabets, special characters, digits , spaces
        3. Remove all vowels
        4. Replaces every consonant by ‘*’''')
    ch=int(input("enter choice: "))
    if ch==1:
        x=input("Enter string: ")
        pali(x)
    elif ch==2:
        x=input("Enter string: ")
        count(x)
    elif ch==3:
        x=input("Enter string: ")
        vow(x)
    elif ch==4:
        x=input("Enter string: ")
        const(x)
    else:
        print("Invalid choice")
        break

