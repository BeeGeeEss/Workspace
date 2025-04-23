first_name = "Eric"
famous_person = " Kate Miller-Heidke "
famous_person = famous_person.strip()
message = "I don't need to sleep, to dream"
filename = 'tests.txt'
website = 'https://google.com'

print(f"Hello {first_name}, would you like to learn some Python?")

print(first_name.title())
print(first_name.upper())
print(first_name.lower())
print("Kate Miller-Heidke once said 'I don't need to sleep, to dream'")
print(f"{famous_person} once said '{message}'")
print(famous_person)
print(famous_person.rstrip())
print(famous_person.lstrip())
print(famous_person.strip())
print("Kate\nMiller\tHeidke")
print(website.removeprefix('https://'))
print(filename.removesuffix('.txt'))


favourite_number = 63

# Basic equations
print(4+4)
print(10-2)
print(4*2)
print(24/3)
print(f"My favourite number is... drumroll please.... {favourite_number}!")