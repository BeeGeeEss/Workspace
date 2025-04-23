guests = [
    "Carrie Fisher",
    "Chrissy Amplett",
    "Stockard Channing",
    "Goldie Hawn",
]
print(guests)
print(len(guests))

print(f"Dear {guests[0]} you are invited to my dinner party!")
print(f"Dear {guests[1]} you are invited to my dinner party!")
print(f"Dear {guests[2]} you are invited to my dinner party!")
print(f"Dear {guests[3]} you are invited to my dinner party!")

print("Goldie Hawn cant attend anymore")
cancelled_guest = guests.pop(3)
print(len(guests))

print("We got a bigger table more guests are welcome!")


print(f"Dear {guests[0]} you are invited to my dinner party!")
print(f"Dear {guests[1]} you are invited to my dinner party!")
print(f"Dear {guests[2]} you are invited to my dinner party!")

guests.insert(0, "Dana Delaney")
guests.insert(2, "Sasha Alexander")
guests.insert(5, "Jessica Capshaw")

print(guests)
print(len(guests))


print(f"Dear {guests[0]} you are invited to my dinner party!")
print(f"Dear {guests[1]} you are invited to my dinner party!")
print(f"Dear {guests[2]} you are invited to my dinner party!")
print(f"Dear {guests[3]} you are invited to my dinner party!")
print(f"Dear {guests[4]} you are invited to my dinner party!")
print(f"Dear {guests[5]} you are invited to my dinner party!")




print("I'm so sorry - turns out I only have space for two guests!")

cancelled_guest_2 = guests.pop(0)
print(f"Sorry I can't invite you {cancelled_guest_2}!")
cancelled_guest_3 = guests.pop(2)
print(f"Sorry I can't invite you {cancelled_guest_3}!")
cancelled_guest_4 = guests.pop(1)
print(f"Sorry I can't invite you {cancelled_guest_4}!")
cancelled_guest_5 = guests.pop(2)
print(f"Sorry I can't invite you {cancelled_guest_5}!")

print(guests)
print(len(guests))

print(f"Don't stress Carrie Fisher and Stockard Channing, you're still invited!")

del guests[0]
del guests[0]

print(guests)
print(len(guests))