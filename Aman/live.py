import mysql.connector as ms
kj = ms.connect(
    host='10.10.8.138',
    password='12345',
    user='root',
    database='grade12'
)

k = kj.cursor()

k.execute('update marks set name = "arjun" where id = 1')
kj.commit()

