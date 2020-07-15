"""def book_description(book_type, author_name):
    print("\nThis book is a " + book_type + " book.")
    print("\nThe author of this book is " + author_name + ".")
book_description(book_type='Thriller', author_name='Dan Brown')
book_description(author_name='Dan Brown', book_type='Thriller')
                    or
"""
def book_description(book_type, author_name='Dan Brown'):
    print("\nThis book is a " + book_type + " book.")
    print("\nThe author of this book is " + author_name + ".")
book_description('Thriller')
