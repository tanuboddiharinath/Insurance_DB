import main as sql
query = """
SELECT A.COMPANY_ID, SUM(AMOUNT) AS TOTAL_AMT FROM INSURANCE_MAIN A 
INNER JOIN PREM_TRANSACTION B ON A.POLICY_ID = B.POLICY_ID 
GROUP BY A.COMPANY_ID 
"""
def three():
    try:
        sql.cur.execute(query)
        d = list(sql.cur.fetchall())
        for i in d:
            print(i)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    three()