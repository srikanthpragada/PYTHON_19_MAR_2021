import requests


def jsonformat(jdict, f):
    if type(jdict) == list:
        for n in jdict:
            jsonformat(n, f)
            # for key, value in n.items():
            # print(f"{key:30} {value}")
    else:
        for key, value in jdict.items():
            if type(value) == dict:
                print(f"{key:30}")
                jsonformat(value, f)
            else:
                f.write(f"{key}, {value}")
                print(f"{key:30} {value}")




resp = requests.get(
    "https://api.github.com/users/srikanthpragada/repos")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()
details = resp.json()  # Convert json to dict
# print(details)
f = open("json_output_file.txt", "wt")
jsonformat(details, f)
f.close()

