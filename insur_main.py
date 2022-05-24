query = """CREATE TABLE INSURANCE_MAIN
(
	POLICY_ID INT PRIMARY KEY AUTO_INCREMENT,
    START_DATE DATE NOT NULL,
	CUST_ID INT,
    COMPANY_ID INT,
    TYPE_ID INT,
    AMT_PREMIUM BIGINT NOT NULL,
    SUM_INSURED BIGINT NOT NULL,
    POLICY_STATUS VARCHAR(30) NOT NULL,
    FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(CUST_ID),
    FOREIGN KEY(COMPANY_ID) REFERENCES COMPANIES(COMPANY_ID),
    FOREIGN KEY(TYPE_ID) REFERENCES INSURANCE_TYPES(TYPE_ID),
    CHECK( AMT_PREMIUM > 200),
    CHECK( SUM_INSURED > 0),
    CHECK( POLICY_STATUS IN ('ACTIVE','INACTIVE'))
);"""

import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
cur.execute(query)