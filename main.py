import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'INSURANCE_PROJ')
cur = mydb.cursor()
query = input()
cur.execute(query)
print(cur.fetchall())
