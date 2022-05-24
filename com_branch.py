query = """CREATE TABLE COM_BRANCH(
BRANCH_NAME VARCHAR(25) PRIMARY KEY,
COMPANY_ID INT,
REGION_ID INT,
FOREIGN KEY (COMPANY_ID) REFERENCES COMPANIES(COMPANY_ID), 
FOREIGN KEY (REGION_ID) REFERENCES REGION(REGION_ID) 
);"""
import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
cur.execute(query)