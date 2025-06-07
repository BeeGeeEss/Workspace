print("Please give me two numbers & I'll add them!")
print("Enter 'quit' to quit the game")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'quit':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'quit':
        break
    try:
        answer = int(first_number) + int(second_number)  
    except ValueError:
        print("You can only use numbers!") 
    else:
        print(answer)   