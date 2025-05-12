#This exercise applies a break statement to a while loop in a function:

def shopping_list():
    prompt_phrase = ("Enter an item to add to your shopping list. (Enter 'quit' to end.): ")
    item_list = []

    while True:
        input_phrase = input(prompt_phrase)

        if input_phrase == 'quit':
            break
        
        else:
            item_list.append(input_phrase)
            print(item_list)

shopping_list() 



#This exercise is to filter through a list, use cintinue to skip bad words,
#store good words in a list

def string_filter(list_of_words):

    result = []

    for word in list_of_words:
        if word in ["heck", "darn"]:
            continue
        
        result.append(word)

    print(result)
    return result        

string_filter(['heck'])
string_filter(['yellow'])
string_filter(['darn'])
string_filter(['submarine'])


#This exercise is to use enumerate for the first multiple of 3 in that list    
def threeven(some_list):

    for index, value in enumerate(some_list):
        if not value % 3:
            return index
    

    return None
        

print(threeven([5, 6, 7, 8, 9]))
print(threeven([1, 2, 4, 5, 7, 8]))
print(threeven([]))



#This excercise is to go through a loop a7 count c's:

def count_the_cs(some_list):
    result = 0

    # your code here...
    for string in some_list:
        for letter in string:
            if letter in "cC":
                result += 1

    return result

print(count_the_cs(["these", "are", "strings"]))
print(count_the_cs(["concatenate", "concentrate", "Cecelia"]))
print(count_the_cs(["nothing to SEE here", "cCcCcCcC"]))

            
