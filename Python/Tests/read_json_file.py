import json
    
    
with open("users.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)
    print(data)