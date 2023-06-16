import json 

open_users = open('users.json') 
data = json.load(open_users) 

for name in data ['first_name']: 
    print(name) 

open_users.close()  