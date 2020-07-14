prompt = "\nEnter 'q' to end this program"
prompt += "\nWhat's the name of your book you read ?_"

while True:
    book = input(prompt)
    if book == 'q':
        break
    else:
        print("You have recently read " + book.title())