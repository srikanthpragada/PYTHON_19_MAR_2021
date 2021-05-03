import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, "html.parser")
links = []
for atag in bs.find_all("a"):
    href = atag['href']
    if href == "#":
        continue

    if not href.startswith("http"):
        href = "http://www.srikanthtechnologies.com/" + href

    if href not in links:
        links.append(href)

for link in links:
    print(link)
