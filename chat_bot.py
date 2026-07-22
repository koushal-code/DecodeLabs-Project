#simple rule based AI chat bot that responds to predefined user inputs
from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M:%S")

# commands that the bot understands
response = {
    'hello' : "Hi there, how's your day going on",
    'hi' : 'hello, how are you?',
    'bye' : 'Goodbye! 👋',
    'exit' : 'exiting...',
    'help' : 'list of commands : \n1. "Hello"\n2. "what is the time?"\n3. "what are you?"\n4. "bye"\n',
    'what is the time?' : f"the time is {time} and date is {now:%A, %B%d} . ",
    'what are you?' : "I'm a simple rule based chatbot",
    'ok' : '. . . ',
    'good' : 'glad to hear 😁'



}

print("\nBot active : type help, for more info...")

while True:
    #user input
    user_input = input('\nYou: ')
    clean_input = user_input.lower().strip()

    #response
    reply = response.get(user_input, 'I did not understand.')
    print(f"Bot: {reply}")

    if clean_input == "bye":
        break
    if clean_input == "exit":
        break

print("\t\n Bot inactive ")
