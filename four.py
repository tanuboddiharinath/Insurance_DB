import main as sql
# import mysql.connector as connection
# mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'INSURANCE_PROJ')
# cur = mydb.cursor()
query = """
SELECT * FROM (
    SELECT B.INSURANCE_NAME,B.TYPE_ID, DENSE_RANK() OVER(partition by B.TYPE_ID ORDER BY COUNT(B.TYPE_ID) DESC) AS RNK
    FROM INSURANCE_MAIN A INNER JOIN INSURANCE_TYPES B ON A.TYPE_ID = B.TYPE_ID
    
)X
WHERE X.RNK = 1 
"""
def four():
    sql.cur.execute(query)
    for i in sql.cur:
        print(i)
if __name__ == "__main__":
    four()