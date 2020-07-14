
in_stock = ['blue pens', 'paper', 'staples']

shopping_cart = ['blue pens', 'paper', 'staples', 'pins']

for item in shopping_cart:
    if item in in_stock:
        print("Adding " + item + " to your cart")
    else:
        print("Sorry " + item + " not in stock")
print("Your order is complete!!!")