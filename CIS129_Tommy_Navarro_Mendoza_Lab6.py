# Tommy Navarro Mendoza
# March 31, 2024
# CIS 129 Lab 6
# The hotdog calculator

import math

def main():
    # // Local variable for the total number of hot dogs needed.
    total = getTotalHotDogs()

    # Named constants for the package sizes
    DOGS = 10
    BUNS = 8

    # Local variables
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

    # Calculations
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = math.ceil(total / DOGS)
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = math.ceil(total / BUNS)

    # Output
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

"""
The getTotalHotDogs module gets the number of people
attending the cookout and the number of hot dogs each
person will be given, and stores the product in the
totalHotDogs reference variable.
"""
def getTotalHotDogs():
    # Local variables
    people = 0
    hotDogs = 0

    # Get the number of people attending the cookout.
    people = int(input('Enter the number of people attending the cookout: '))

    # Get the number of hot dogs each person will be given.
    hotDogs = int(input('Enter the number of hot dogs for each person: '))

    # Calculate the total number of hot dogs needed
    total = people * hotDogs
    return total

"""
The showResults module accepts the total number of hot dogs
as an argument and calculates the minimum packages of hot
dogs and hot dog buns, the left over hot dogs and hot dog
buns, and displays the results.
"""
def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    # Display the minimum packages of hot dogs needed.
    print('Minimum packages of hot dogs needed:', minDogs)
    # Display the minimum packages of buns needed.
    print('Minimum packages of hot dog buns needed:', minBuns)
    # Display the number of hot dogs left over.
    print('Hot dogs left over:', dogsLeft)
    # Display the number of hot dog buns left over.
    print('Hot dog buns left over:', bunsLeft)

# Call function for test
main()
