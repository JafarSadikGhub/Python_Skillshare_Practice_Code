import json

filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\phone_number.json"

with open(filename) as file_object:
    phone_numbers = json.load(file_object)

print(phone_numbers)
