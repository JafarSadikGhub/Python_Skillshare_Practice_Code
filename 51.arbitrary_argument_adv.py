def assign_seat(seat, *requests):
    print("\nAssign seat number " + str(seat) + " the following request(s):")
    for request in requests:
        print("- " + request)

assign_seat(25, 'window seat')
