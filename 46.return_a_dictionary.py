def build_book(name, author, publisher):
    book = {'name' : name, 'author' : author, 'publisher' : publisher}
    return book

my_book = build_book('The vinci Code', 'Dan Brown', 'Doubleday')
print(my_book)