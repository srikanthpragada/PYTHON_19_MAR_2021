import requests
from bs4 import BeautifulSoup
from datetime import datetime


def getfulldate(stdate):
    year = datetime.now().year
    stdate = stdate + "-" + str(year)
    return datetime.strptime(stdate, '%d-%b-%Y')


resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, "html.parser")
table = bs.find('table', id='ctl00_ContentPlaceHolder1_GridView2')
# print(table.text)
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    sdate = getfulldate(stdate)
    nodays = (sdate - datetime.now()).days
    if nodays > 0:
        msg = "days to go"
    else:
        msg = "days old"

    print(f"{title:30} {timings:10} {stdate:10} {abs(nodays):2} {msg}")
