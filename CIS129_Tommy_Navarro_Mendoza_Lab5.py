# Lab 5 The Bottle Return Program
# Tommy Navarro Mendoza
# March 27, 2024
"""This program helps keep track of the total number of bottles collected for seven days, and calculate the total payout."""

# Delclare variables
total_bottles = 0 
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"

# Loop to run program again
while keep_going == "y":
    # Get bottles code
    while counter < 8:
        today_bottles = int(input('Enter the number of bottles for today: '))
        total_bottles += today_bottles
        counter += 1
        # Calculate payout
        total_payout = total_bottles * 0.10

    # Print information
    print(f'The total number of bottles collected is {total_bottles}')
    print(f'The total paid out is $ {total_payout:.2f}')

    # Resetting variables for next iteration
    total_bottles = 0 
    counter = 1
    today_bottles = 0
    total_payout = 0

    # Asking the user if they want to continue
    keep_going = input("Do you want to enter another week's worth of data?\n(Enter y or n): ")

