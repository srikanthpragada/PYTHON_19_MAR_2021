# Convert Employees table to JSON

import sqlite3
import json

employees = []
con = sqlite3.connect("hr.db")
cur = con.cursor()
cur.execute("select * from employees")  # SQL Command

for id, name, job, salary in cur.fetchall():
    employees.append({"id": id, "name": name, "job": job, "salary": salary})

print(json.dumps(employees))
