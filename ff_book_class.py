class Book():
    """Methods"""
    def __init__(self, name, price, publisher):

        self.name = name
        self.price = price
        self.publisher = publisher

    def hardback(self):
        print(self.name.title() + " is a hardback book.")
    
    def softback(self):
        print(self.name.title() + " is a softback book. ")
    
    def ebook(self):
        print(self.name.title() + " is an ebook.")
    
    def ebook_reader(self):
        print("Library: " + self.name.title()+ ", " + self.price + ", " + self.publisher.title() + ".")
    
"""Instance"""
my_book = Book('the vinci code', 'RS512', 'Doubleday')
your_book = Book('the godfather', '$9.99', 'virgin books')

"""Accessing attributes"""
print("I am currently reading " + my_book.name.title() + ".")
print("This book cost " + my_book.price + ".")

"""Accessing Methods"""
my_book.softback()
my_book.hardback()
my_book.ebook_reader()
your_book.softback()

