import sqlite3

con = sqlite3.connect("hr.db")
cur = con.cursor()
cur.execute("select count(id), sum(salary), avg(salary) from employees")
count_employees, totalsalary, avgsalary = cur.fetchone()

print(f'No. of employees : {count_employees:10}')
print(f'Total salary     : {totalsalary:10}')
print(f'Avg. salary      : {avgsalary:10.0f}')

cur.close()
con.close()
