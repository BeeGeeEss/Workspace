#zHandling errors:
try:
    with open('cats.txt', 'r', encoding='utf-8') as file:
        for item in file:
            print(f"{item.strip()}")
     
     
    with open('dogs.txt', 'r', encoding='utf-8') as file:
        for item in file:
            print(f"{item.strip()}")

except FileNotFoundError:
    print("Sorry this file doesn't exist!")


#Failing silently:
try:
    with open('cats.txt', 'r', encoding='utf-8') as file:
        for item in file:
            print(f"{item.strip()}")
     
     
    with open('dogs.txt', 'r', encoding='utf-8') as file:
        for item in file:
            print(f"{item.strip()}")

except FileNotFoundError:
    pass
