import pandas as pd
import maininse as sql

# mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'INSURANCE_PROJ')
# cur = mydb.cursor()
df = pd.read_csv(r"csv_files\customer.csv")
insert_query = "INSERT INTO CUSTOMER VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
l = []
for i in df.values:
    l.append(tuple(i))
sql.cur.executemany(insert_query,l)
sql.mydb.commit()
