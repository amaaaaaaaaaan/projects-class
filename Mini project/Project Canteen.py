import mysql.connector as ms
import csv
db=ms.connect(host="localhost", user="root", passwd="12345", database="CANTEEN")
cu=db.cursor()
cu.execute("select * from fafo")
x=cu.fetchall()
tot=0
while True:
    print("---------------MENU----------------")
    print("S.No \tItem\tPrice\tQuantity")
    for i in x:
        print(i)
    ch=int(input("Enter choice: "))
    if ch==4:
        break
    cu.execute(f"select ItemID,ItemName,Price from fafo where ItemID={ch}")
    ite=cu.fetchone()
    print(ite)
    qt=int(input("Enter quantity: "))
    cu.execute(f"update fafo set quantity=quantity-{qt} where ItemId={ch}")
    db.commit()
    tot+=qt*ite[2]

print(f"Total cost is: {tot}")
f=open("Sales.csv","w",newline="")
cs=csv.writer(f)
cs.writerow(f"Amount is:{tot}")




    
             
        

