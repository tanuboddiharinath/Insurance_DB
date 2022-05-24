import pandas as pd
import maininse as sql
insert_query = 'INSERT INTO branch_details VAlUES(%s,%s,%s)'
l = []
df = pd.read_csv(r"csv_files\branch_details.csv")
for i in df.values:
    l.append(tuple(i))
sql.cur.executemany(insert_query,l)
sql.mydb.commit()