#This is an excercise in changing list order

countries = [
    "North Korea",
    "United States",
    "Guantanamo Bay",
    "Russia",
    "China",
]

print("Here is the list")
print(countries)
print("\nHere is the sorted list")
print(sorted(countries))
print("\nHere is the original list again")
print(countries)
print("\nHere is the list reveresed")
countries.reverse()
print(countries)
print("\nHere is the list reveres-reverse")
countries.reverse()
print(countries)
print("\nHere is the countries sorted alphabetically")
countries.sort()
print(countries)
print("\nHere is the list sorted in reverse alphabetical order")
countries.sort(reverse=True)
print(countries)

# This is list slicing:

print("The first three items in the list are...")
print(countries[:3])

print("The last three items in the list are...")
print(countries[-3:])

print("The middle three items in the list are...")
print(countries[1:4])
