def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nWhat's your name? ")
    print("Press 'q' anytime to quit this program.")
    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break
    
    formatted_name = get_formatted_name(first_name, last_name)
    print("Welcome " + formatted_name + ".")