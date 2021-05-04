import sqlite3

con = sqlite3.connect("hr.db")
cur = con.cursor()
cur.execute("select * from employees") # SQL Command

for id, name, job, salary in cur.fetchall():
    print(f"{id:2} {name:20} {job:10} {salary:10}")
