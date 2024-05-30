import mysql.connector as ms 
db=ms.connect(host="localhost",user="root",password="12345",database="automobile")
cu=db.cursor()



def display():
    cu.execute("select * from car_den")
    x=cu.fetchall()
    for i in x:
        print(i)


def diac():#ACCEPT new car details and DISPLAY all records
    cc=int(input("Enter code: "))
    cn=input("Enter car name: ")
    co=input("Enter company name: ")
    col=input("Enter colour of car: ")
    ca=int(input("Enter capcity: "))
    ch=int(input("Enter charge: "))
    cu.execute(f"insert into car_den values({cc},'{cn}','{co}','{col}',{ca},{ch})")
    db.commit()
    display()


diac()