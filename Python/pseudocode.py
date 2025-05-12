def current_day(user_input):

    if user_input == "Wednesday":
        print("It's Wednesday!")
    
    else:
        user_input = " "
        while not user_input.lower().endswith("y"):
            user_input = input("What day is it?: ")
        
        if user_input == "Wednesday":
            print("Haha, you're a funny one! See ya!")
        else:
            print(f"Thankyou for letting me know that today is {user_input}! See ya!")


#current_day("Wednesday")
current_day(" ")
# current_day("Thursday")