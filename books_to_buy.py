def books_available(*books):
    for book in books:
        """print("The following title is available to buy " + book + ".")"""
        books_in_stock = "The following title is available to buy " + book.title() + "."
        print(books_in_stock)

def books_description(author_name, book_type= "non-fiction"):
    print("\nThis is a " + book_type + " book.")
    print("The author of this book is " + author_name.title())

