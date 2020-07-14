admin_users = ['shoshi', 'jafar']
username = input("Please enter your username: ")
if username not in admin_users:
    print("You do not have access")
else:
    print("Access granted")