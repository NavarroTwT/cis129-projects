# My Coffee and Muffin Shop
# This program calculates and displays the receipt for coffee and muffin purchases,
# including itemized costs, tax, and the total amount.

# Declare variables and constants
priceOfCoffee = 5
priceOfMuffin = 4
taxPercent = 0.06


# Get input from customer
print('***************************************')
print('My Coffee and Muffin Shop')

# Get input for the number of coffees and muffins
coffee_amt = int(input('Number of coffees bought?\n'))
muffin_amt = int(input('Number of muffins bought?\n'))
print('***************************************')


# Calculating costs
coffeeTotal = coffee_amt * priceOfCoffee
muffinTotal = muffin_amt * priceOfMuffin
tax = (coffeeTotal + muffinTotal) * taxPercent
totalCost = coffeeTotal + muffinTotal + tax


# Display the receipt to the customer
print('\n***************************************')
print('My Coffee and Muffin Shop Receipt')

# Display the individual item costs
print(coffee_amt,'Coffee at $',priceOfCoffee,'each: $',coffeeTotal)
print(muffin_amt,'Muffins at $',priceOfMuffin,'each: $',muffinTotal)
print('6% tax: $',tax)

# Display the total cost
print('---------')
print('Total: $',totalCost)
print('***************************************')
