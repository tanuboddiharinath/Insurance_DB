import pandas as pd
import maininse as sql
# import mysql.connector as connection
# mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
# cur = mydb.cursor()
insert_query = 'INSERT INTO COMPANIES VALUES(%s,%s)'
l = []
df = pd.read_csv('csv_files\compines.csv')
for i in df.values:
    l.append(tuple(i))
sql.cur.executemany(insert_query,l)
sql.mydb.commit()