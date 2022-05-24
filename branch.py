import pandas as pd
import maininse as sql

df = pd.read_csv(r"csv_files\branch.csv")
insert_query = "INSERT INTO COM_BRANCH VALUES (%s,%s,%s)"
l = []
for i in df.values:
    l.append(tuple(i))
sql.cur.executemany(insert_query,l)
sql.mydb.commit()