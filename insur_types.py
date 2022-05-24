import mysql.connector as connection
mydb = connection.connect(host = 'localhost',username = 'root',passwd = 'mysql',database = 'insurpract')
cur = mydb.cursor()
query ="""CREATE TABLE INSURANCE_TYPES
(
	TYPE_ID INT PRIMARY KEY AUTO_INCREMENT,
    INSURANCE_NAME VARCHAR(30) NOT NULL,
    CHECK(INSURANCE_NAME IN ('HEALTH_INSURENSE','MOTOR_VECHILE_INSURENSE','TERM_INSURENSE','TRAVEL_INUSURENSE','HOME_INSURENSE'))
);"""

cur.execute(query)