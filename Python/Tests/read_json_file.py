"""import JSON module to read and write"""
import json


with open("users.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)
    print(data)

new_user = {
    "Name": "John Smith",
    "email": "john@smith.com",
    "is_admin": False
}

def add_user():
    data.append(new_user)
    with open("users.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    add_user()
