#One user adding one name to a file

# Prompt the user for their name
name = input("Welcome! What's your name? ")

# Open the file in append mode so we don't overwrite previous entries
with open("new_guests.txt", mode="a", encoding="utf-8") as file:
    file.write(name + "\n")

print(f"Thanks, {name}! Your name has been added to the guest list.")



#Multiple users adding their names to a guestbook
while True:
    name = input("Enter your name (or type 'quit' to stop): ").strip()

    if name.lower() == "quit":
        print("Goodbye!")
        break

    with open("new_guestbook.txt", mode="a", encoding="utf-8") as file:
        file.write(name + "\n")
    
    print(f"Thanks, {name}! Your name has been added to the guestbook.")
