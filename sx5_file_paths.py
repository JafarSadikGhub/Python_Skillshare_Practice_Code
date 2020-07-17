"""with open('files/copy_of_movies.txt') as file_object:
    contents = file_object.read()
    print(contents.strip())"""
### Using absolute file path:

file_path = 'C:\\Users\\USER\Desktop\\Python_Skillshare_Code_Repo\\files\\copy_of_movies.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.strip())