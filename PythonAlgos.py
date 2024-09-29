# Cheks Either a number is prime or not .
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# To cheks Either The Number is Palindromic or Not  . 
def check_is_palindromic(n) :
    original = str(n)
    reversed_str = original[::-1]  # Reverse the string
    return  original == reversed_str 



        