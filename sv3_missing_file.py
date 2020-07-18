filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\Jafarf.txt"

try:

    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
        message = "Sorry, the file " + filename + " cannot be found."
        print(message)

