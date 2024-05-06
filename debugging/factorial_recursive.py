#!/usr/bin/python3

import sys

# Function description:
# This function calculates the factorial of a given integer using recursion.

def factorial(n):
    # Parameters:
    # n (int): The integer for which the factorial is to be calculated.
    
    # Returns:
    # int: The factorial of the input integer n.
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Takes the integer input from the command line argument, calculates its factorial, and prints it.
f = factorial(int(sys.argv[1]))
print(f)

