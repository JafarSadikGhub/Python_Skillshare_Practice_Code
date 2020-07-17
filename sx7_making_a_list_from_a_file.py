filename = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\movies_line_by_line.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
    """the readline() takes each line from the file and stores
    it in a list""" 

for line in lines:
    print(line.strip())
    """The above loop prints each contents from the list"""

print(type(lines))