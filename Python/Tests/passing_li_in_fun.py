# #This excercise passes a list to a function
# #Function:
def show_messages(messages):

    for message in messages:
        print(message)
# #List:
msg = ['Hello, how are you?', 'It\'s all coming up tickety boo', 'Marvelous, old chap']
show_messages(msg)


def send_messages(show_messages, sent_messages):

    while show_messages:
        current_messages = show_messages.pop()
        print(f"Sending Messages: {current_messages}")
        sent_messages.append(current_messages)

def show_sent_messages(sent_messages):
        
    for sent_message in sent_messages:
        print(f"The following messages have been sent: {sent_message}")

show_messages = ['Hello, how are you?', 'It\'s all coming up tickety boo', 'Marvelous, old chap']       
sent_messages = []

#To create a copied list for 'show_messages'
send_messages(show_messages[:], sent_messages)
show_sent_messages(sent_messages)

#Check that the original list is still in tact:
#print(show_messages)