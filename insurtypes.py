import pandas as pd
import maininse as sql
# mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
# cur = mydb.cursor()
df = pd.read_csv(r"csv_files\branch_details.csv")
insert_query = "INSERT INTO BRANCH_DETAILS VALUES (%s,%s,%s)"
l = []
for i in df.values:
    l.append(tuple(i))
sql.cur.executemany(insert_query,l)
sql.mydb.commit()


