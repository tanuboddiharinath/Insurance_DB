import main as sql


# import mysql.connector as connection
# mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'INSURANCE_PROJ')
# cur = mydb.cursor()
query = """
SELECT * FROM (
SELECT C.COMPANY_NAME, RANK() OVER(ORDER BY COUNT(B.POLICY_ID) DESC) AS RNK FROM COMPANIES C 
INNER JOIN INSURANCE_MAIN B ON C.COMPANY_ID = B.COMPANY_ID 
GROUP BY C.COMPANY_ID
)X 
WHERE X.RNK = 1
"""
def six():
    sql.cur.execute(query)
    for i in sql.cur.fetchall():
        print(i)
if __name__ == "__main__":
    six()