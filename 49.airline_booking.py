def passengers(not_checked_in, checked_in):
    while not_checked_in:
        current_passenger = not_checked_in.pop()
        print(current_passenger.title() + " is not checked in.\nChecking in the passenger...")
        checked_in.append(current_passenger)

def show_checked_in_passengers(checked_in):
    print("\nThe following passengers are currently checked in: ")
    for individual in checked_in:
        print(individual.title())

def show_not_checked_in_passengers(not_checked_in):
    print("\nThe following passengers are currently not checked in: ")
    for individual in not_checked_in:
        print(individual.title())

not_checked_in = ['nusrat', 'jahan', 'shoshi', 'maya', 'jafar', 'sadik']
checked_in = []
#passengers(not_checked_in, checked_in)
#show_checked_in_passengers(checked_in)
"""In any case if we want not to modify the original list, 
we could just call the function by the copy of the list.
for instance, """
passengers(not_checked_in[:], checked_in)
show_checked_in_passengers(checked_in)
show_not_checked_in_passengers(not_checked_in)
