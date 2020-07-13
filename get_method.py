terms = {'integer' : 'A whole number.', 'string' : 'a sequence of characters.'}

print(terms.get('integer'))
print(terms.get('float'))
del terms['integer']
print(terms)