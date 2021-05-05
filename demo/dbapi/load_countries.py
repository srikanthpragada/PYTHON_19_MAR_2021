import requests
import sqlite3

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

con = sqlite3.connect("hr.db")
cur = con.cursor()
# Delete all rows from COUNTRIES -  delete from countries
count = 0
for c in countries:
    try:
        cur.execute("insert into countries values(?,?,?,?)",
                    (c['alpha3Code'], c['name'], c['capital'], c['population']))
        count += 1
    except:
        pass

con.commit()
print(f"Loaded {count} countries!")
cur.close()
con.close()
