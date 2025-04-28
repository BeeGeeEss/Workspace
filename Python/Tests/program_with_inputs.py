# This is an excercise in inputs (excercise in terminal) 

prompt = ("Please enter your choice of rental car!: ")

car = input(prompt)
print(f"\nLet me see if I can find you a {car}")




number = input("How many guests are you booking for? ")
number = int(number)

if number <= 8:
    print("You're table is ready!")
else:
    print("You'll have to wait!")



number = input("Enter a number and I will tell you if it's a mutliple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number is a multiple of 10!")
else:
    print(f"\nThe number is not a multiple of 10!")