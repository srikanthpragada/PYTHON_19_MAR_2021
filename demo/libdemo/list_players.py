from datetime import datetime, timedelta

f = open("players.txt", "rt")
players = {}
for line in f:
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    try:
        # convert string to datetime
        dob = datetime.strptime(parts[1], "%d-%m-%Y")
        # Calculate age in years
        age = (datetime.now() - dob).days // 365
        players[parts[0]] = age
    except:
        pass

f.close()

for name, age in sorted(players.items(), key=lambda t: t[1], reverse=True):
    print(f"{name:20} {age:2}")
