def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):

    entry_ticket_cost = 10 if age >= 60 else 15
    candy_cost = 5 if has_membership else 10
    parking_cost = 3 if transport_type == "Car" else 0


    result = calculate_total_cost_of_visiting_cinema(20, True, "Car")
    print(f"{entry_ticket_cost} + {candy_cost} + {parking_cost}")
   