query = """CREATE TABLE CLAIM_TXN
(
	CLAIM_TXN_ID BIGINT PRIMARY KEY AUTO_INCREMENT,
    POLICY_ID INT,
    CUST_ID INT,
    CLAIMED_AMT BIGINT NOT NULL,
    CLAIMED_DATE DATE NOT NULL,
	FOREIGN KEY(POLICY_ID) REFERENCES INSURANCE_MAIN(POLICY_ID),
    FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(CUST_ID)
);"""

import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
cur.execute(query)