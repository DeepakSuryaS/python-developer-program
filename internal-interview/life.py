import sqlite3
import csv

conn = sqlite3.connect(database="../internal-interview/test_db_1.db") # if db doesn't exist, it'll be automatically created in the specified path.
cur = conn.cursor()

# Country,Year,life,population,income,region
cur.execute(""" CREATE TABLE COUNTRIES(Country VARCHAR2(32), Year VARCHAR2(32), life VARCHAR2(32), population VARCHAR2(32), income VARCHAR2(32), region VARCHAR2(32)) """)

with open('../internal-interview/gapminder.csv','r') as fin: 
    dr = csv.DictReader(fin) 
    to_db = [(i['Country'], i['Year'], i['life'], i['population'], i['income'], i['region']) for i in dr]

cur.executemany("INSERT INTO COUNTRIES (Country, Year, life, population, income, region) VALUES (?, ?, ?, ?, ?, ?);", to_db)
conn.commit()


cur.execute(''' SELECT * FROM COUNTRIES ORDER BY life DESC ''')
rows = cur.fetchall()
for i in rows:
    print(i)


conn.close()
