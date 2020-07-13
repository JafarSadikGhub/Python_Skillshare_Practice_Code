book_0 = {
    'name' : 'Da Vinci Code',
    'author' : 'Dan Brown',
    'publisher' : 'Anchor Books',
    'price' : 'RS.895',
}
book_1 = {
    'name' : 'Da Vinci Code',
    'author' : 'Dan Brown',
    'publisher' : 'Anchor Books',
    'price' : 'RS.895',
}
book_2 = {
    'name' : 'Da Vinci Code',
    'author' : 'Dan Brown',
    'publisher' : 'Anchor Books',
    'price' : 'RS.895',
}
books = [book_0, book_1, book_2]
#print(books)
stock_items = []

for blue_pen in range(0, 50):
    new_blue_pen = {'color' : 'blue', 'type' : 'ballpoint', 'price' : '5'}
    stock_items.append(new_blue_pen)
#print(stock_items)
for blue_pen in stock_items[0:5]:
    if blue_pen['price'] == '5':
        blue_pen['price'] = '3.5' 
for blue_pen in stock_items[0:10]:
    print(blue_pen)