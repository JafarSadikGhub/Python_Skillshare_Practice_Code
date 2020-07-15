def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

teacher = formatted_name('Mohammed', 'Sadik', 'Jafar')
print(teacher)
teacher = formatted_name('Mohammed', 'Sadik')
print(teacher)