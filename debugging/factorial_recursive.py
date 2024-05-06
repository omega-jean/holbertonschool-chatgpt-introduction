#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursive approach.

    Function Description:
    Recursively computes the factorial of a given non-negative integer 'n'.
    The factorial of a non-negative integer 'n' is the product of all positive integers less than or equal to 'n'.

    Parameters:
    n (int): A non-negative integer for which the factorial needs to be calculated.

    Returns:
    int: The factorial of 'n'. If 'n' is 0, the factorial is 1 (0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extract the integer argument from the command line and compute its factorial
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)
