terms = {}

terms['variable'] = 'Represents or refers to a value stored in memory'
terms['integer'] = 'A whole number'

print(terms['variable'])
print(terms['integer'])
#print(terms['float'])


if 'variable' in terms:
    print("I know what a variable is, it is: " + terms['variable'])
else:
    print("I have no idea what it is.")

if 'float' in terms:
    print("I know what float is, it is: " + terms['float_d_k'])
else:
    print("I have no idea what it is.")
    choice = input("Do you want to define this key? [Y]/N?")
    if choice == 'Y' or choice == 'y':
        float_d_k = input("Input the key name:")
        #x = float_d_k
        terms['float_d_k'] = input("Input the defination to the key " + float_d_k + " :")
        #terms[x] = float_d_d
        print("I know what float is, it is: " + terms['float_d_k'])