# This excercise is to create dictionaries in a list:

friend_1 = {
    'first_name' : 'Rachael', 
    'last_name' : 'Gait', 
    'age' : '53',
    'city' : 'Vic',
    'favourite_numbers' : '7',
    }

friend_2 = {
    'first_name' : 'Brando', 
    'last_name' : 'Smith', 
    'age' : '34',
    'city' : 'Vic',
    'favourite_numbers' : ['63', '64', '73', '74'],
    }

friend_3 = {
    'first_name' : 'Britt', 
    'last_name' : 'Williams', 
    'age' : '28',
    'city' : 'Vic',
    'favourite_numbers' : '10',
    }

peoples = [friend_1, friend_2, friend_3]

for people in peoples:
    print(people)


# This excercise is to create a list in a dictionary:

for favourite_number in ['favourite_numbers']:
    print(f"{friend_1['first_name']}'s favourite number is {friend_1['favourite_numbers']}")

for favourite_number in ['favourite_numbers']:
    print(f"The favourite number of {friend_2['first_name']} is {friend_2['favourite_numbers']}")

for favourite_number in ['favourite_numbers']:
    print(f"The favourite number of {friend_3['first_name']} is {friend_3['favourite_numbers']}")





