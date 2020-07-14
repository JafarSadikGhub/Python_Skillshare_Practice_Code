registered_names = ['nusrat', 'jahan', 'shoshi', 'maya', 'jafar', 'sadik']

username = input("Please enter the username you would like to use: ")

if username in registered_names:
    print("Sorry, the username is already taken")
else:
    registered_names.append(username)
    print(registered_names)