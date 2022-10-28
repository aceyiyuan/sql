#https://docs.python.org/3/library/sqlite3.html
#sql.exe
"""
****************sqlite***********************
import sqlite3
con = sqlite3.connect(r'db_conn.sqlite')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS movie")
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")


res = cur.execute("SELECT name FROM sqlite_master")
row=res.fetchone()
if row:
    print(f'Tietokannassa on olemassa tämä taulu :{row[0]}')
else:
    print(f'Tietokannassa ei ole taulua')

cur.execute('''
    INSERT INTO movie VALUES 
        ('Monthy Python and the Holy Grail',1975, 8.2),
        ('And now for something completely differenet',1971, 7.5)

'''
)


con.commit()
res=cur.execute("SELECT score FROM movie")
for row in res.fetchall():
    score=row[0]
    print(f'Elokuvan arvosant on {score}')


data=[
    ('Monthly Python live at the Hollywood Bowl', 1982, 7.9),
    ("Monthly python's The meaning of life",1983, 7.5),
    ("Monthly python's life of Brian", 1979,8.0),# tässä voi jäätä , python kielessä ei haita

]

cur.executemany("INSERT INTO movie VALUES (?,?,?)",data)

con.commit() #ilman tätä riviä, ei näe muutosta
#res=cur.execute("SELECT * FROM movie")

res=cur.execute("SELECT * FROM movie  order by year")
#First alternative

#for row in res.fetchall():
    #nimi=row[0]
    #vuosi=row[1]
    #score=row[-1]

#second alternative

#for row in res.fetchall():

    #title, year, _=row # _ single underline wildcard

# third alternative
for title, year, _ in res.fetchall():
    #print(f'Elokuvan nimi on {nimi} and published year is {vuosi} and score is {score}')
    print(f'Elokuva {title} on vuodesta {year}')

res=cur.execute("SELECT title, year,MAX(score) FROM movie")
#res=cur.execute("SELECT * FROM movie ORDER BY score DESC LIMIT 1") #toinen vaihtoehto
title, year,score=res.fetchone()
print(f"Paras Monty Pythoin elokuva on '{title}' vuodesta {year} and {score}")

"""


