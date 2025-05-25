#This exercise is to create a dice and roll it to get a random number

# from random import randint
# """Pulling the randon integar function from the random module library"""

# class Die:
#     """Class of dice"""

#     def __init__(self, sides=20):
#         self.sides = sides
        
#     def roll_die(self):
#         return randint(1, self.sides)

# my_roll = Die()

# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())
# print(my_roll.roll_die())

from random import choice

lottery = (1, 7, 8, 11, 63, 74, 7, 19, 77, 20, 'B', 'R', 'A', 'N')

"""Regular lottery draw"""
draw1 = choice(lottery)
draw2 = choice(lottery)
draw3 = choice(lottery)
draw4 = choice(lottery)

print(draw1)
print(draw2)
print(draw3)
print(draw4)
print(f"Any ticket matching these letters/numbers: {draw1}, {draw2}, {draw3}, {draw4} wins")

"""Lottery analysis trying to find my ticket"""
my_ticket = ('B', 7, 63, 8)

attempts = 0
found = False

while not found:
    attempts += 1
    draw = tuple(choice(lottery) for _ in range(len(my_ticket)))
    if draw == my_ticket:
        found = True

print(f"Winning ticket matched after {attempts} attempts: {draw}")

