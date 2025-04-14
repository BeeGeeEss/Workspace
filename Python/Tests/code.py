def calculate_rocket_fuel_required(distance):
    fuel = distance * 15
    if fuel < 100:
        return 100
    else:
        return fuel
   
result = calculate_rocket_fuel_required(20)
print(f"fuel required for 20 units of distance: {result}")