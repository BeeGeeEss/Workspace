#This excercise is to move intems from one list to another:

sandwich_orders = ["Pastrami", "Pastrami", "Pastrami", "Tuna", "Egg Lettuce", "Salami"]
# finished_sandwiches = []

# while sandwich_orders:
#     creating_orders = sandwich_orders.pop()

#     print(f"Making your {creating_orders.title()}")
#     finished_sandwiches.append(creating_orders)

# print("\nThe following sandwiches have been made:")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

#This excercise is to remove all instances of a value

print(sandwich_orders)

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)

