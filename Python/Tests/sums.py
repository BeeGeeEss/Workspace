# #This is stock standard addition:

# def add_numbers(x, y):
#     return x + y



#Use a while loop to write a function that calculates and returns the sum of 
# all integers up to and including 100.

# def sum_to_one_hundred():

#     result = 0
#     count = 0

#     # insert your code here...
#     while count < 101:
#         result += count
#         count += 1
   

#     return result

# print(sum_to_one_hundred())


#Specifically, can you make it so that the function calculates the sum 
# of all integers up to (and including) a target value

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


#Write a function that asks the user to input a number from 1 to 100 
# (inclusive). If the user supplies a value outside that range, the function 
# should print an error message and prompt the user to try again

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



# def calculate_total_cost_of_visiting_cinema(age, has_membership, transport_type):
#     entry_ticket_cost = 10 if age >= 60 else 15
#     candy_cost = 5 if has_membership else 10
#     parking_cost = 3 if transport_type == "Car" else 0

#     result = entry_ticket_cost, candy_cost, parking_cost 
#     print(result)

#     result = entry_ticket_cost+ candy_cost+ parking_cost 

#     print(result)

# calculate_total_cost_of_visiting_cinema(20, True, "Car")
# calculate_total_cost_of_visiting_cinema(65, False, "Bus")
# calculate_total_cost_of_visiting_cinema(45, False, "Car")
# calculate_total_cost_of_visiting_cinema(60, True, "Car")




#Use a for loop to write a function that calculates and returns the sum of 
# all integers up to and including 100.

# def sum_to_one_hundred():
#     result = 0
#     # insert your code here...
#     for x in range(1, 101, 1):
#         result += x
#     return result

# result = sum_to_one_hundred()
# print(result)



#Write a function that repeatedly asks the user for an integer, 
# adding that number to a total each time, until the user gives the input "end"

# def sum_of_inputs():
    
#     total = 0
#     user_number = 0

#     # your code here...
#     while True:
#         user_number = input("Enter a number (or 'end' to finish): ")
#         if user_number == 'end':
#             break
#         total += int(user_number)
#     return total

# print(sum_of_inputs())


#Create a function that sums every integer up to the value it receives 
#as an argument.

# def sum_to_x(target_integer):
#     result = 0

#     for x in range(1, target_integer +1):
#         result += x
#     return result

# result = sum_to_x(4)
# print(result)


#Write a function that accepts a list of integers as an argumemt, and 
# returns the sum of all even numbers in the list.

# def sum_of_evens(input_list):
#     result = 0
    
#     # your code here...
#     for element in input_list:
#         if element % 2 == 0:
#             result += element
#     return result

# print(sum_of_evens([]))
# print(sum_of_evens([7, 9, 11]))
# print(sum_of_evens([2, 6, 14]))




LIST_OF_WORDS = [
    "serendipity",
    "petrichor",
    "supine", 
    "solitude",
    "aurora",
    "idyllic",
    "clinomania",
    "pluviophile",
    "euphoria",
    "sequoia"
]

def filter_list(some_string): 
    output_list = []

    for word in LIST_OF_WORDS:
        if some_string in word:
            output_list.append(word)

    return output_list


print(filter_list('aaa'))
print(filter_list('ph'))
print(filter_list('i'))
print(filter_list('q'))



   
    

