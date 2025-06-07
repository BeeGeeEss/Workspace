import json
from pathlib import Path

#Getting a favourite number, storing it and retriving it.
print("Please give me your favourite number!")

while True:
    favourite_number = input("\nFavourite number: ")
    if favourite_number == 'quit':
        break

    with open("favourite_number.json", mode="w", encoding="utf-8") as file:
        json.dump(favourite_number, file)

    print(f"Thanks! I saved your favourite number: {favourite_number}")
    break

with open("favourite_number.json", mode="r", encoding="utf-8") as file:
    loaded_number = json.load(file)

print(f"I know your favourite number it's {loaded_number}")





#The pathlib way to either retrieve a users favourite number or ask for one
file_path = Path("favourite_number.json")

# Step 1: Try to read the saved number
if file_path.exists():
    with open(file_path, mode="r", encoding="utf-8") as file:
        favourite_number = json.load(file)
    print(f"I know your favourite number — it's {favourite_number}!")
else:
    print("I don't know your favourite number yet!")
    favourite_number = input("Please enter your favourite number: ")
    
    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(favourite_number, file)
    
    print(f"Thanks! I saved your favourite number: {favourite_number}")
