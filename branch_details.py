query = """CREATE TABLE BRANCH_DETAILS(
ID INT PRIMARY KEY AUTO_INCREMENT,
BRANCH_NAME VARCHAR(25),
INSURANCE_TYPE_ID INT,
FOREIGN KEY (BRANCH_NAME) REFERENCES COM_BRANCH(BRANCH_NAME),
FOREIGN KEY (INSURANCE_TYPE_ID) REFERENCES INSURANCE_TYPES(TYPE_ID)
);"""

import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
cur.execute(query)