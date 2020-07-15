def seat_profile(first, last, **passenger_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in passenger_info.items():
        profile[key] = value
    return profile
passenger_profile = seat_profile('Jafar', 'Sadik', seat_number = 25, breakfast_order = 'Yes')
print(passenger_profile)