import json

username = input("What is your username? ")

filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\username.json"

with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("Thank you, I'll remember you when you'll come back!")
    
