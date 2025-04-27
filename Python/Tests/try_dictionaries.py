#This excercise is to loop throgh information in a dictionary:

# friend = {
#     'first_name' : 'Rachael', 
#     'last_name' : 'Gait', 
#     'age' : '53',
#     'city' : 'Vic',
#     }

# for key, value in friend.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


glossary = {
    'lower' : 'To change the sensitivity of words to lower case',
    'upper' : 'To change the sensitivity of words to upper case',
    'title' : 'To change the sensitivity od words to be title case'
    }

# for key, value in glossary.items():
#      print(f"\nKey: {key}")
#      print(f"\tValue: {value}")

for word in glossary.keys():
    print(word.title())

for definition in glossary.values():
    print(definition.title())