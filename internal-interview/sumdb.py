import sqlite3
import csv

conn = sqlite3.connect(database="../internal-interview/test_db_2.db") # if db doesn't exist, it'll be automatically created in the specified path.
cur = conn.cursor()


# Country,Year,life,population,income,region
cur.execute(""" CREATE TABLE CANDIDATES(ID INT, NAME VARCHAR2(32), TEST1 VARCHAR2(32), TEST2 VARCHAR2(32), INTERVIEW1 VARCHAR2(32), TOTAL VARCHAR2(32)) """)


# cur.executemany("INSERT INTO COUNTRIES (Country, Year, life, population, income, region) VALUES (?, ?, ?, ?, ?, ?);", to_db)

cur.execute("INSERT INTO CANDIDATES (ID, NAME, TEST1, TEST2, INTERVIEW1, TOTAL) VALUES (101, 'A', 10, 10, 30, 0);")
cur.execute("INSERT INTO CANDIDATES (ID, NAME, TEST1, TEST2, INTERVIEW1, TOTAL) VALUES (102, 'B', 5, 5, 20, 0);")
conn.commit()

cur.execute(''' SELECT TEST1,TEST2,INTERVIEW1,(TEST1 + TEST2 + INTERVIEW1) as 'Total' FROM CANDIDATES; ''')
rows = cur.fetchall()
for i in rows:
    print(i)
    


conn.close()
