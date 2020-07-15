def book_available(books):
    for book in books:
        """print("The following title is available to buy " + book + ".")"""
        books_in_stock = "The following title is available to buy " + book.title() + "."
        print(books_in_stock)

available = ['elon musk', 'the vinci code', 'angels and demons', 'the godfather']
book_available(available)