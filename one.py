import main as sql
query = """
    SELECT COMPANY_NAME FROM COMPANIES A 
    INNER JOIN COM_BRANCH B ON
    A.COMPANY_ID = B.COMPANY_ID INNER JOIN
    INSURANCE_MAIN C ON A.COMPANY_ID = C.COMPANY_ID
    WHERE B.REGION_ID = 1
    GROUP BY A.COMPANY_ID
    HAVING COUNT(DISTINCT C.TYPE_ID)>3 
    """
def one():
    sql.cur.execute(query)
    print(sql.cur.fetchall())
    for i in sql.cur:
        print(i)

if __name__ == "__main__":
    one()