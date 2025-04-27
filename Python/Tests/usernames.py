# This excercise is to use if statements to apply different conditions to
# different users:

usernames = ['admin', 'brucelee', 'charazar', 'candlemaker', 'fettywap']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username} thank you for logging in again")


# This excercise to test is a list is empty:

usernames = []

if usernames:
    for username in usernames:
        print(f"Hello {usernames}!")
else: 
    print("We need to find some users!")


#This excercise is to cross-check two lists (ensuring case sensitivity):

current_users = ['admin', 'brucelee', 'charazar', 'candlemaker', 'Fettywap']

current_users = [user.lower() for user in current_users]


new_users = ['fettywap', 'Charazar', 'mulan', 'barbzz', 'plant_girl']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("You will need to enter a new username!")
    else:
        print("This username is available!")


# If-elif-else:

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")