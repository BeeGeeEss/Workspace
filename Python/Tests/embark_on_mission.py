def ready_to_embark_on_mission(have_supplies, distance_to_mission_site, fuel_in_vehicle):
    fuel_in_vehicle >= (distance_to_mission_site * 2)

    if have_supplies == False: 
        return False 
    if have_supplies == True and distance_to_mission_site <= 10:
        return True
    if distance_to_mission_site >= 10 and fuel_in_vehicle >= (distance_to_mission_site * 2):
        return True
    elif distance_to_mission_site >= 10 and fuel_in_vehicle <= (distance_to_mission_site * 2):
        return False

    

result = ready_to_embark_on_mission(False, 1, 100)
print(f"It is {result} that I am ready to embark on this mission")

result = ready_to_embark_on_mission(True, 1, 100)
print(f"It is {result} that I am ready to embark on this mission")

result = ready_to_embark_on_mission(True, 5, 0)
print(f"It is {result} that I am ready to embark on this mission")

result = ready_to_embark_on_mission(True, 20, 30)
print(f"It is {result} that I am ready to embark on this mission")

result = ready_to_embark_on_mission(True, 20, 40)
print(f"It is {result} that I am ready to embark on this mission")

result = ready_to_embark_on_mission(True, 100, 300)
print(f"It is {result} that I am ready to embark on this mission")



