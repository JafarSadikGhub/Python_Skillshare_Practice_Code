message = input("What is your favorite film? ")
print(message.title())

filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\favorite_film.txt"

with open(filename, 'a') as file_object:
    file_object.write(message + "\n")
