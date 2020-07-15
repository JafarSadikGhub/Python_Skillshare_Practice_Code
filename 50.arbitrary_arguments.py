def create_passenger(*requests):
    # *requests will create a tuple
    print("\nThis passenger has requested: ")
    # print(requests)
    for request in requests:
        print("- " + request)


create_passenger('window seat', 'top of plane', 'breakfast')
