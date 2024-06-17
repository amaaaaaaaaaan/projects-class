import random as rd
on=0
tw=0
th=0
fo=0
fi=0
si=0
for i in range(50):
    rg=rd.randrange(1,7)
    if rg==1:
        on+=1
    elif rg==2:
        tw+=1
    elif rg==3:
        th+=1
    elif rg==4:
        fo+=1
    elif rg==5:
        fi+=1
    elif rg==6:
        si+=1
print(f'''
No of occurences of each number on the dice is:
    1-{on}
    2-{tw}
    3-{th}
    4-{fo}
    5-{fi}
    6-{si}''')
