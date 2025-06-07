#counting words in a book:
with open("pride_and_prejudice.txt", "r", encoding='utf-8') as file:
     content = file.read().lower()

word_to_count = "love"
word_count = content.split().count(word_to_count)
print(f"The word {word_to_count} appears {word_count} times in this book!")



#counting words in a row in a book:
with open("pride_and_prejudice.txt", "r", encoding='utf-8') as file:
     content = file.readline()

line = "five sisters and a cousin. And when the party entered the assembly-room, it consisted of only five altogether: Mr. Bingley, his two sisters" 
print(line.lower().count('sisters'))

