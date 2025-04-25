#This is an excercise in looping and cubing:

numbers = list(range(1, 21))
print(numbers)

big_numbers = list(range(1, 1_000_001))

for number in big_numbers:
    print(f"{big_numbers} - look we're counting!")
    break

print(big_numbers)

print(min(big_numbers))
print(max(big_numbers))
print(sum(big_numbers))


odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

multiples_of_three = list(range(3, 31, 3))

for multiple in multiples_of_three:
    print(f"{multiple} - I'm a multiple of three!")


cubes = [value**3 for value in range(1, 11)]
print(cubes)