current_num = 1
while current_num<= 10:
    print(current_num)
    current_num +=1
prompt1 = "Enter your name. Press 'q' to exit the program : "
name = ""
while name != 'q':
    name = input(prompt1)
    if 'q' not in name:
        print("The name you entered is: " + name)