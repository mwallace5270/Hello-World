import json 

open_users = open(users.json) 
data = json.load(open_users) 

for i in data ['first_name']: 
    print(i) 

open_users.close()  