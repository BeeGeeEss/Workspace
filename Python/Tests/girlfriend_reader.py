# from pathlib import Path

# path = Path('girlfriend.txt')
# contents = path.read_text()
# print(contents)


# from pathlib import Path

# path = Path('girlfriend.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)


# from pathlib import Path

# path = Path('girlfriend.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line

# print(pi_string)
# print(len(pi_string))



from pathlib import Path
"""Replace contents in file"""

path = Path('girlfriend.txt')
contents = path.read_text()


print(contents.replace('girlfriend', 'theyfriend'))


"""Writing to a file"""
#Will write over other text better to do this with blank file

#path.write_text("words")