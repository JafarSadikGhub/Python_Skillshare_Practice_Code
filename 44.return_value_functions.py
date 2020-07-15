def formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

teacher = formatted_name('jafar', 'sadik')
print(teacher)

def get_formatted_useremail(email_address):
    useremail = email_address.strip()
    return useremail
user = get_formatted_useremail('jafar.sadik@nsu.edu   ')
print(user)