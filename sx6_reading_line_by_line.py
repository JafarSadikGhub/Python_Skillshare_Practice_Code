file_path = "C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\movies_line_by_line.txt"

with open(file_path) as file_object:
    for content_line in file_object:
        print(content_line.strip())
        