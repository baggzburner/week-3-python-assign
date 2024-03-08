

def calculate_discount (price, discount_percent): 
    price = float(input('what is the price of the product? \n'))

    discount_percent = float(input('enter the discount percentage \n'))

    if(discount_percent>=0.20):
        discount = price*discount_percent
        new_price = price - discount
        return new_price 
    else:
        return price
    

print(calculate_discount(10.87, 50.9))