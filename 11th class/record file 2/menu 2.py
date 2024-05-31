print(" 1.Accept a string and count the number of vowels and consonants in the string.\n 2.Accept a string and remove vowels from the string.\n 3.Accept a string or sentence and count all the words that are used to form that string.")
ch=int(input("enter choice"))
if ch==1:
    input = input("Enter a string: ")
    vowels = 0
    consonants = 0
    for char in input:
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
elif ch==2:
    string = input("Enter a string: ")
    result= ""
    for char in string:
        if char not in "aeiou":
            result += char
    print("String without vowels:", result)
elif ch==3:
    input = input("Enter a string or sentence: ")
    count = 0
    for char in input:
        if char.isspace():
            count += 1
    count += 1
    print("Number of words:", count)


