# My Coffee and Muffin Shop
# This program calculates and displays the receipt for coffee and muffin purchases,
# including itemized costs, tax, and the total amount.

# Declare variables and constants
priceOfCoffee = 5
priceOfMuffin = 4
priceOfCake = 6
priceOfCookie = 1
taxDecimal = 0.06
taxPercent = round(taxDecimal * 100)


# Get input from customer
print('***************************************')
print('My Coffee and Muffin Shop')

# Get input for the number of coffees and muffins
coffee_amt = int(input('Number of coffees bought?\n'))
muffin_amt = int(input('Number of muffins bought?\n'))
cake_amt = int(input('Number of cakes bought?\n'))
cookie_amt = int(input('Number of cookies bought?\n'))
print('***************************************')


# Calculating costs
coffeeTotal = coffee_amt * priceOfCoffee
muffinTotal = muffin_amt * priceOfMuffin
cakeTotal = cake_amt * priceOfCake
cookieTotal = cookie_amt * priceOfCookie
tax = round((coffeeTotal + muffinTotal + cakeTotal + cookieTotal) * taxDecimal, 2)
totalCost = coffeeTotal + muffinTotal + cakeTotal + cookieTotal + tax


# Display the receipt to the customer
print('\n***************************************')
print('My Coffee and Muffin Shop Receipt')

# Display the individual item costs
print(coffee_amt,'Coffee at $',priceOfCoffee,'each: $',coffeeTotal)
print(muffin_amt,'Muffins at $',priceOfMuffin,'each: $',muffinTotal)
print(cake_amt,'Cakes at $',priceOfCake,'each: $',cakeTotal)
print(cookie_amt,'Cookies at $',priceOfCookie,'each: $',cookieTotal)
print(taxPercent,'% tax: $',tax)

# Display the total cost
print('---------')
print('Total: $',totalCost)
print('***************************************')

# Thank the user
print('Thank you for choosing My Coffee and Muffin Shop! We appreciate your business and look forward to serving you again.')
