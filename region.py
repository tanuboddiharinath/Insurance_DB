import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
query ="""CREATE TABLE REGION 
(
	REGION_ID INT PRIMARY KEY AUTO_INCREMENT ,
    CITY_ID INT ,
    REGION_NAME VARCHAR(25) NOT NULL,
    CHECK (REGION_NAME IN ('NORTH','SOUTH','EAST','WEST')),
    FOREIGN KEY(CITY_ID) REFERENCES CITY(CITY_ID)
);"""

cur.execute(query)