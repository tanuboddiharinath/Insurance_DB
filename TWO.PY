import main as sql
query = """
SELECT * FROM (
    SELECT A.COMPANY_NAME,DENSE_RANK() OVER(ORDER BY COUNT(B.TYPE_ID) DESC) AS RNK FROM COMPANIES A
    INNER JOIN INSURANCE_MAIN B ON A.COMPANY_ID = B.COMPANY_ID 
    GROUP BY B.TYPE_ID 
)X
WHERE X.RNK = 1
"""
def two():
    try:
        sql.cur.execute(query)
        for i in sql.cur.fetchall():
            print(i)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    two()