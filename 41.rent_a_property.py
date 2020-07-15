rental_properties = {}
rental_open = True

while rental_open:
    username = input("\nWhat's your name? ")
    rental_property = input("What's the address of the property you want to rent? ")

    rental_properties[username] = rental_property

    repeat = input("\nDo you know anyone who might like to rent? ")
    if repeat == 'no':
        rental_open = False

print("\n--- Property to rent ---")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " to rent.")