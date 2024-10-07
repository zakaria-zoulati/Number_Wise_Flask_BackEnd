"""

ALL The Functions defined below will serve as a utility functions . 


"""

import math  


# The utility number : 1  
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x


# This is The utility Number : 2 
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  
        number //= 10 
    return total












