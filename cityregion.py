import pandas as pd
import maininse as sql
df = pd.read_csv('csv_files\city.csv')
l = []
for i in df.values:
    l.append(tuple(i))
print(l)
insert_querycity = f"""INSERT INTO CITY VALUES {(l[0][0],l[0][1])}"""
mydb = sql.connection.connect(host ="localhost",username ="root",passwd = "mysql",database = 'insurpract')
cur = mydb.cursor()
cur.execute(insert_querycity)
mydb.commit()


