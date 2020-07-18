import json

phone_numbers = [1234567890]

filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\phone_number.json"

with open(filename, 'w') as file_object:
    json.dump(phone_numbers, file_object)
    