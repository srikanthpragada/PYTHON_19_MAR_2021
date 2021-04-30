import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

details = resp.json()  # Convert json to dict

for name, value in details.items():
    print(f"{name:30} {value}")
