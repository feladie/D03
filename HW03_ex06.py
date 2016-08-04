#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
###############################################################################
# Exercise 6.2
# See 6.1: "write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y."
# When you submit only include your final function: compare

"""Compares the value of two values: Returns 1 if the first is greater than the second; Returns
    0 if the two values are equal; Returns -1 if the first is less than the second."""

def compare(x, y):
    if (x > y): 
        return 1
    elif (x == y):
        return 0
    elif (x < y):
        return -1    

###############################################################################
# Exercise 6.2
# See 6.2: "use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments."
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share in your final push your incremental
# work.

"""Given the two legs of a right triangle, returns the hypotenuse of the triangle."""

import math

def hypotenuse(side1, side2):
    side1_sq = side1**2 
    side2_sq = side2**2
    hypotenuse_sq = side1_sq + side2_sq
    return math.sqrt(hypotenuse_sq)


###############################################################################
# Exercise 6.4
# See 6.4: "write a function is_between(x, y, z) that returns True if x <= y <= z
# or False otherwise"
# When you submit only include your final function: is_between

"""Returns true if the values of the arguments are in ascending order or false otherwise."""

def is_between(x, y, z):
    if (x <= y and y <= z):
        return True
    else:
        return False

###############################################################################
# Exercise 3.2
# See "Exercise 3, part 2": "Write a function called is_palindrome that takes a
# string argument and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a
# string."
# When you submit only include your final function: is_palindrome

"""Returns true if the string argument is a palindrome."""

def is_palindrome(str):
    length = len(str) 

    if (length > 1) and (str[0] == str[length - 1]): # If not the middle letter and symmetric letters are the same
        return is_palindrome(str[1:(length - 1)])
    elif (length > 1) and (str[0] != str[length - 1]): # If not the middle letter and symmetric letters are not equal
        return False
    else:   # When middle letter, returns True
        return True

###############################################################################
# Exercise 4
# See "Exercise 4": "A number, a, is a power of b if it is divisible by b and
# a/b is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b. Note: you will have to think
# about the base case."
# Note: Please use the provided definition and only plan for positive integers
# (whole numbers not including zero)
# When you submit only include your final function: is_power


"""Determines whether or not a is a power of b."""

def is_power(a, b):
    quotient = a / b # Quotient of a and b
    if (a == b): # Base case
        return True
    elif (a % b == 0 and quotient % b == 0): # If a is divisble by b and the quotient is divisible by b.
        return True
    else:
        return False

###############################################################################
def main():
    """Your functions will be called within this function."""
    ###########################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")






    ###########################################################################
    # # Uncomment the below to test and before commiting:
    # Exercise 1
    print(compare(1, 1))
    print(compare(1, 2))
    print(compare(2, 1))
    # # Exercise 2
    print(hypotenuse(1, 1))
    print(hypotenuse(3, 4))
    print(hypotenuse(1.2, 12))
    # # Exercise 3
    print(is_between(1, 2, 3))
    print(is_between(2, 1, 3))
    print(is_between(3, 1, 2))
    print(is_between(1, 1, 2))
    # # Exercise 6
    print(is_palindrome("Python"))
    print(is_palindrome("evitative"))
    print(is_palindrome("sememes"))
    print(is_palindrome("oooooooooooo"))
    # # Exercise 7
    print(is_power(28, 3))
    print(is_power(27, 3))
    print(is_power(248832, 12))
    print(is_power(248844, 12))


if __name__ == "__main__":
    main()
