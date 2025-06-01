import json
    
    
with open("users.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)
    print(data)

def add_user():
    pass


if __name__ == '__main__':
    add_user()
