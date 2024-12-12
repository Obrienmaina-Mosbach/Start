try:
    amount = input('What is your the price before VAT tax?\n')
    product_amount = int(amount)
    tax = 0.07
    total = product_amount + product_amount * tax

    print("This is the price including VAT: " + str(total))
except ValueError: #A try-except block catches invalid input, such as text instead of a number.
    print('Enter a valid number')