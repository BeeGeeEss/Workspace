import random

def get_input(prompt):
    """Takes input from the user, based on a prompt."""
    # This function is used every single time the program gets input from the user!
    input_value = input(prompt)
    
    return input_value

def get_a_number(prompt):
    """Repeatedly requests input from the user until they supply something that can be converted to an integer or type 'quit'."""
    while True:
        user_input = get_input(prompt)
        if user_input.strip().lower() == "quit":
            return None
        try:
            return int(user_input)
        except ValueError:
            print("That wasn't a number, please try again.")

def guess_the_number(the_number):
    """Runs a single game of guess the number - asking for guesses until correct or quit."""
    while True:
        user_guess = get_a_number("Guess the number I'm thinking of!: ")
        if user_guess is None:
            print("You chose to quit. Goodbye!\n")
            return  # Exit this round
        if user_guess == the_number:
            print(f"That's correct! It was {the_number}!\n")
            return
        else:
            print("That wasn't quite right, try again!")

def prompt_play(text_insert):
    """Invites the user to play the game."""
    # We don't convert the input to a number here, but we still use get_input!
    choice = get_input(f"""Let's play {text_insert} game! I'll think of a number between 0 and 10, and you have to guess it. You can quit any time by typing 'quit'.
Press Enter to begin: """)

def main_loop():
    """The main loop of the game - invites the user to play again over and over until they quit."""
    # We are using the text_insert variable to make sure our grammar is correct.
    # On the first loop we invite the user to play *a* game.
    text_insert = "a"
    while True:
        prompt_play(text_insert)
        # After the first loop we invite them to play *another* game.
        text_insert="another"
        guess_the_number(random.randint(0, 10))
        
main_loop()