# This excercise is in while loops and breaks

prompt = "Pizza topping? "
prompt += "\nEnter quit when you are finished. "

active = True
while active:
    message = input(prompt)
    

    if message =='quit':
        active == False
        break
    else:
        print(message)