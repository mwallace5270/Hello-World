import json

open_users = open("users.json")
data = json.load(open_users)

for name in data:
    print(name["first_name"])

open_users.close()
