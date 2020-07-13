my_ordered_car = {
    'type' : 'standard four saloon',
    'extras' : ['alloy wheels', 'climate control', 'leather interior']
}
print('The car you ordered is a ' + my_ordered_car['type'] + ' with extra following features: ')

for extra in my_ordered_car['extras']:
    print("\t" + extra)