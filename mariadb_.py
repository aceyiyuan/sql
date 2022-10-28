
#käynnistä xampp xampp-control.exe
#start apache and mysql
#click Apache admin phpmyadmin

# Connect to MariaDB Platform

import mariadb
import sys

try:
    conn=mariadb.connect(
        user="root",
        password="",
        host='127.0.0.1',
        port=3306,
        database="harjoitus"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS movie")
cur.execute("""
      create table if not exists movie(
        title VARCHAR(255),
        year SMALLINT,
        score FLOAT
      )
      
      """)

cur.execute('''
    INSERT INTO movie VALUES 
        ('Monthy Python and the Holy Grail',1975, 8.2),
        ('And now for something completely differenet',1971, 7.5)

'''
)
conn.commit()
cur.execute("SELECT score FROM movie")
#print(cur.fetchall())
#for row in cur.fetchall(): can also write as follows 
for row in cur:
    print(f'Elokuvan arvosana on ({row[0]}')

data=[
    ('Monthly Python live at the Hollywood Bowl', 1982, 7.9),
    ("Monthly python's The meaning of life",1983, 7.5),
    ("Monthly python's life of Brian", 1979,8.0),# tässä voi jäätä , python kielessä ei haita

]

cur.executemany("INSERT INTO movie VALUES (?,?,?)",data)

conn.commit() #ilman tätä riviä, ei näe muutosta
cur.execute("SELECT * FROM movie  order by year")
#First alternative

for row in cur.fetchall():
    nimi=row[0]
    vuosi=row[1]
    score=row[-1]
print(f"Paras Monty Pythoin elokuva on '{nimi}' vuodesta {vuosi} and {score}")