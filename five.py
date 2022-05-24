import main as sql
# import mysql.connector as connection
# mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'INSURANCE_PROJ')
# cur = mydb.cursor()
query = """
SELECT C.CUST_NAME FROM CUSTOMER C 
INNER JOIN INSURANCE_MAIN B ON C.CUST_ID = B.CUST_ID 
GROUP BY C.CUST_ID 
HAVING COUNT(TYPE_ID)>2
"""
def five():
    sql.cur.execute(query)
    for i in sql.cur.fetchall():
        print(i)

if __name__ == "__main__":
    five()