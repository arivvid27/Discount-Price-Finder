# This is where python gets the info for the price
price = float(input('What price is the object? (Without the "$" sign) '))

# This is where python gets info about the discount
percent = int(input('What percent off is your coupon? (Without the "%" sign) '))

# This is where it all happens
step1 = (percent / 100)
step2 = (step1 * price)
step3 = (price - step2)

# This is how you see the discounted price
print(f'''This is your price:
{step3}''')