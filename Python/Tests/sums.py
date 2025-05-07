#This is stock standard addition:

# def add_numbers(x, y):
#     return x + y




# def sum_to_one_hundred():

#     result = 0
#     count = 0

#     # insert your code here...
#     while count < 101:
#         result += count
#         count += 1
   

#     return result

# print(sum_to_one_hundred())




# def sum_to_x(target_integer):
    
#     count = 0
#     result = 0

# # ... your code here...
#     while count <= target_integer:
#         result += count
#         count += 1
#     return result

# print(sum_to_x(3))
# print(sum_to_x(4))
# print(sum_to_x(100))


# def input_within_range():
#     MIN_VALUE = 1
#     MAX_VALUE = 100

#     user_number = 0

#     while user_number < MIN_VALUE or user_number > MAX_VALUE:
#         user_input = int(input("Please enter a number between 1 and 100: "))
#         if user_number < MIN_VALUE:
#             print("ERROR: That value is too low!")
#         if user_number > MAX_VALUE:
#             print("ERROR: That value is too high!") 

#     return user_number

# print(input_within_range())



def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):
    entry_ticket_cost = 10 if age >= 60 else 15
    candy_cost = 5 if has_membership else 10
    parking_cost = 3 if transport_type == "Car" else 0

    result = entry_ticket_cost, candy_cost, parking_cost 
    
    print(result)

    result = entry_ticket_cost+ candy_cost+ parking_cost 

    print(result)

calculate_total_cost_of_visiting_cinema(20, True, "Car")
calculate_total_cost_of_visiting_cinema(65, False, "Bus")
calculate_total_cost_of_visiting_cinema(45, False, "Car")
calculate_total_cost_of_visiting_cinema(60, True, "Car")





   
    

