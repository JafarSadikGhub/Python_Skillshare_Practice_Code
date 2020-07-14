prompt = "\nEnter 'q' to end this program"
prompt += "\nWhat's your name?_"

active = True

while active:
    message = input(prompt)
    if message == 'q':
        active = False
    else:
        print(message)