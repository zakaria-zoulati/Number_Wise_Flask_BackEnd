"""
   
    NUMBER THEORY ALGORITHMS 


"""


from utilities import is_perfect_square , sum_of_digits
import math 



# This is The algo : 1 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# This is The algo : 2 
def is_palindromic(n) :
    original = str(n)
    reversed_str = original[::-1]  # Reverse the string
    return  original == reversed_str 


# Ths is The algorihm number : 3 
def is_fibonacci(n):
    if( n <=0  ) : 
        return False 
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)




# This is The algorithm number : 4 
def is_Lucas(number) :
    if number < 0:
        return False
    a, b = 2, 1
    if number == a or number == b:
        return True

    lucas_number = 0
    while lucas_number < number:
        lucas_number = a + b
        a = b
        b = lucas_number

        if lucas_number == number:
            return True
    return False 


# This is The algorithm number : 5
def is_triangular(n):
    discriminant = 1 + 8 * n
    sqrt_discriminant = int(math.sqrt(discriminant))
    return (sqrt_discriminant * sqrt_discriminant == discriminant) and ((-1 + sqrt_discriminant) % 2 == 0)


# This is The algorihm number : 6 
def is_pronic(number):
    if number < 0:
        return False
    n = 0
    while n * (n + 1) <= number:
        if n * (n + 1) == number:
            return True
        n += 1
    return False


# This is The algorithm Number : 7 
def is_polite(n):
    if (n & (n - 1)) == 0:
        return False
    
    return True


# This is The algrithm Number : 8 
def is_perfect(n):
    if n == 1:
        return False
    sum_of_divisors = 1  
    for i in range(2, n):
        if n % i == 0:
            sum_of_divisors += i
            
    return sum_of_divisors == n


# This is the algorithm Number : 9 
def is_pentatope(number):
    if number < 0:
        return False
    
    n = 0
    while True:
        pentatope = (n * (n + 1) * (n + 2) * (n + 3)) // 24
        if pentatope == number:
            return True
        if pentatope > number:
            break
        n += 1
    
    return False


# This is The algorithm Number : 10 
def is_pentagonal(number):
    n = (1 + math.sqrt(1 + 24 * number)) / 6
    return n == math.floor(n) and n > 0


# This is The algorithm Number : 11
def is_octagonal(number):
    if number < 0:
        return False
    n = 0
    while True:
        octagonal = n * (3 * n - 2)
        if octagonal == number:
            return True
        if octagonal > number:
            break
        n += 1
    return False 


# This is The algorihm Number : 12 
def is_icosahedral(number):
    if number < 0:
        return False
    n = 0
    while True:
        first = (5 * n ** 3 - 5 * n ** 2 + 2 * n)
        if first % 2 == 1:
            n += 1
            continue
        icosahedral = first // 2
        if icosahedral == number:
            return True
        if icosahedral > number:
            break
        n += 1
    return False

# This is The algorithm Number : 13 
def is_harshad(number):
    sum_digits = sum_of_digits(number)  
    return number % sum_digits == 0  

# This is The algorithm Number : 14  
def is_fermat(number):
    n = 0
    while True:
        exponent = 2 ** (2 ** n)
        fermat = exponent + 1 
        
        if fermat == number:
            return True  
        elif fermat > number:
            return False  
        
        n += 1  

# This is The algorithm Number : 15 
def is_even(n) : 
    if(  n % 2 == 0  ) :
        return True
    return False 

# This is The algorithm Nunmber : 16 
def is_deficient(n):
    if n < 1:
        return False  
    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors < n

# This is The algorithm Number : 17 
def is_cullen(number):
    n = 0
    while True:
        cullen = n * (2 ** n) + 1
        if cullen == number : 
            return True
        if cullen > number:
            return False
        
        n += 1

# This is The algorithm Number : 18  
def catalan(n):
    numerator = math.factorial(2 * n)
    denominator = math.factorial(n + 1) * math.factorial(n)
    return numerator // denominator
def is_catalan(number):
    i = 0
    while True:
        catalan_number = catalan(i)
        if catalan_number == number:
            return True
        if catalan_number > number:
            return False
        i += 1


# This is The algorithm Number : 19 
def is_automorphic(n):
    square = n * n
    while n > 0:
        if square % 10 != n % 10:
            return False
        square //= 10
        n //= 10
    return True

# This is The algorithm Number : 20 
def is_sphenic(n):
    prime_factors = []
    i = 2

    while i * i <= n:
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
            n //= i
        if len(prime_factors) > 3:
            return False
        i += 1

    if n > 1 and is_prime(n):
        prime_factors.append(n)

    return len(prime_factors) == 3





