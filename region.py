import pandas as pd
import maininse as sql
insert_query = "INSERT INTO REGION VALUES(%s,%s,%s)"
l = []
df = pd.read_csv(r"csv_files\region.csv")
for i in df.values:
    l.append(tuple(i))
sql.cur.executemany(insert_query,l)
sql.mydb.commit()

