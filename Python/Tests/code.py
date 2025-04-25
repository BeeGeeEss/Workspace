# This was the python logic for an ED challenge with control flows:

def calculate_rocket_fuel_required(distance):
    fuel = distance * 15
    if fuel < 100:
        return 100
    else:
        return fuel
   
result = calculate_rocket_fuel_required(1)
print(f"fuel required for 1 units of distance: {result}")

result = calculate_rocket_fuel_required(10)
print(f"fuel required for 10 unit/s of distance: {result}")

result = calculate_rocket_fuel_required(20)
print(f"fuel required for 20 unit/s of distance: {result}")





def calculate_ticket_price_for_performer(regular_ticket_price, performer_type):
   if regular_ticket_price == 100 and performer_type == 'Jugglers':
      return 50
   if regular_ticket_price == 200 and performer_type == 'Magicians':
      return 40
   if regular_ticket_price == 10 and performer_type == 'Tight Rope Walkers':
      return 8
   if regular_ticket_price == 150 and performer_type == 'Escape Artists':
      return 0

result = calculate_ticket_price_for_performer(100, 'Jugglers')
print(f"Price of ticket required for Jugglers: {result}")

result = calculate_ticket_price_for_performer(200, 'Magicians')
print(f"Price of ticket required for Magicians: {result}")

result = calculate_ticket_price_for_performer(10, 'Tight Rope Walkers')
print(f"Price of ticket required for Tight Rope Walkers: {result}")

result = calculate_ticket_price_for_performer(150, 'Escape Artists')
print(f"Price of ticket required for Escape Artists: {result}") # type: ignore