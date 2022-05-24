import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
query ="""CREATE TABLE CITY
(
	CITY_ID INT PRIMARY KEY AUTO_INCREMENT,
    CITY_NAME VARCHAR(50) NOT NULL
);"""

cur.execute(query)