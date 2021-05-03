import requests
from bs4 import BeautifulSoup

website = input("Enter website :")
resp = requests.get(website)
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

bs = BeautifulSoup(resp.text, "html.parser")
links = []
for atag in bs.find_all("a"):
    href = atag['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        if href.startswith("/"):
            href = f"{website}{href}"
        else:
            href = f"{website}/{href}"

    if href not in links:
        links.append(href)

for link in links:
    print(link)
