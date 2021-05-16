import sqlite3

conn = sqlite3.connect('testbase')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS MyKith')
cur.execute('CREATE TABLE MyKith (name TEXT, surname TEXT, sex TEXT, age INTEGER, InviteOrNot BOOLEAN)')
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Ivan", "Loban", "M", 23))
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Lera", "Teacher", "W", 20))
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Vovua", "Lukashevich", "M", 39))
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Yluana", "Suheckaya", "W", 17))
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Daria", "Levin", "W", 19))
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Slavua", "Kosolapov", "M", 39))
cur.execute('INSERT INTO MyKith (name, surname, sex, age) VALUES (?, ?, ?, ?)' , ("Andrey", "Loban", "M", 16))
cur.execute('UPDATE MyKith SET InviteOrNot = 1 WHERE surname = "Levin" OR age BETWEEN 22 AND 24 OR name = "Lera"')
conn.commit()
cur.execute('SELECT name, surname, InviteOrNot  FROM MyKith WHERE InviteOrNot = 1 ')
for row in cur:
    print(row)