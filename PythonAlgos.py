"""
To simply Checkouts The Unit Tests Yiu can Just Run :
>> pytest PythonAlgos.py 

"""

import math 

############################################################################################################################
# Cheks Either a number is prime or not .
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


#For Unit Testing Purpose
def test_is_prime() : 
    assert is_prime(7) == True 
    assert is_prime(21) == False 
    assert is_prime(0) == False  
    assert is_prime(0) == False  
    assert is_prime(100003) == True  

###########################################################################################################################

# To cheks Either The Number is Palindromic or Not  . 
def check_is_palindromic(n) :
    original = str(n)
    reversed_str = original[::-1]  # Reverse the string
    return  original == reversed_str 


# For Unit Testing Purpose
def test_is_palindromic() : 
    assert check_is_palindromic(121) == True
    assert check_is_palindromic(12321) == True
    assert check_is_palindromic(123) == False
    assert check_is_palindromic(-121) == False

###########################################################################################################################

# Function to check if a number is a perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

# Function to check if a number is a Fibonacci number
def is_fibonacci(n):
    if( n <=0  ) : 
        return False 
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)



def test_fibonacci() : 
    assert is_fibonacci(5) == True 
    assert is_fibonacci(2) == True 
    assert is_fibonacci(-1) == False 
    assert is_fibonacci(44444) == False 
    assert is_perfect_square(100) == True  
    assert is_perfect_square(99) == False
    assert is_perfect_square(3) == False

        