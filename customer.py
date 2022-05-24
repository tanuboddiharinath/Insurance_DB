import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
query = """CREATE TABLE CUSTOMER
(
	CUST_ID INT PRIMARY KEY AUTO_INCREMENT,
    CUST_NAME VARCHAR(100) NOT NULL,
    NOMINEE VARCHAR(100),
    NOMINEE_RELATION VARCHAR(50),
    PHN_NO BIGINT NOT NULL,
    ADDRESS VARCHAR(200) NOT NULL,
    DOB DATE NOT NULL
);"""

cur.execute(query)