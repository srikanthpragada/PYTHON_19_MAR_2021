import sqlite3

con = sqlite3.connect("hr.db")
cur = con.cursor()
name = input("Enter name :")
cur.execute(f"select * from countries where name like '%{name}%'") # SQL Command

for country in cur.fetchall():
    print(country[1])

cur.close()
con.close()
