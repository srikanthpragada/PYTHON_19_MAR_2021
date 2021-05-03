import requests

region = input("Enter region :")
resp = requests.get(f"https://restcountries.eu/rest/v2/region/{region}")
countries = resp.json()

for c in sorted(countries, key=lambda d: d['population'], reverse=True):
    area = c['area']
    if area is None:
        area = 0

    print(f"{c['name'][:40]:40} {c['capital']:20} {c['population']:10} {area:10}")
