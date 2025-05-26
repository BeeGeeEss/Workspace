from pathlib import Path

path = Path('pi_digits.txt')

"""1. To read a files contents"""
# contents = path.read_text().rstrip()
# print(contents)

"""2. To read each line in a files contents"""
contents = path.read_text()

lines = contents.splitlines()
# for line in lines:
#     print(line)

"""3. Working with a files contents = create a one line string"""
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

