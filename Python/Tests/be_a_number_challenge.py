def get_a_number(prompt):
    """Repeatedly asks the user for a number until they give an input that can be converted to an integer. Returns an int."""
    result = None
    
    while result is None:
        try:
            user_input = input(prompt)
            result = int(user_input)
        except ValueError:
            print("That wasn't a number, please try again.")
    return result


user_input = get_a_number("Please enter an integer: ")
print(f"Your number was: {user_input}.")