import json

filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\username.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)
        #print("Welcome back, " + username + "!")

except FileNotFoundError:
    username = input("What is your username? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("Thank you, I will remember you when you'll come back!")

else:
    print("Welcome back, " + username + "!")