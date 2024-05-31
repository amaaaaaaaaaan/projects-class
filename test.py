import mysql.connector as ms
db=ms.connect(host='localhost',user='root',password='12345',database='DosaAir')
cr=db.cursor()
cr.execute("insert into login values('Aman Shooja',12345)")
cr.execute("insert into login values('Mahadev Maneesh',46755432)")
db.commit()
cr.execute("select * from login")
print (cr.fetchall())
cr.close()