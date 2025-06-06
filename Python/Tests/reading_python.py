#Read entire file
with open("learning_python.txt", "r", encoding='utf-8') as file:
     content = file.read()
     print(content)

#Replace word in file
print(content.replace('python', 'C#'))

#Read file line by line through a for loop
lines = content.splitlines()
for line in lines:
    line_by_line = line.strip()
    print(line_by_line)

#simplifying the code above
for line in content.splitlines():
     line_by_line = line.strip()
     print(line_by_line)
