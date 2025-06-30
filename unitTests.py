"""
This is Where I gonna define all The unit tests . 

"""

from PythonAlgos import *

# The Test Number : 1 
def test_is_prime() : 
    assert is_prime(7) == True 
    assert is_prime(21) == False 
    assert is_prime(0) == False  
    assert is_prime(0) == False  
    assert is_prime(100003) == True  


# The test Number : 2  
def test_is_palindromic() : 
    assert is_palindromic(121) == True
    assert is_palindromic(12321) == True
    assert is_palindromic(123) == False
    assert is_palindromic(-121) == False

# The test Number : 3
def test_perfect_square() : 
    assert is_perfect_square(100) == True  
    assert is_perfect_square(99) == False
    assert is_perfect_square(3) == False


# The test Number : 4  
def test_fibonacci() : 
    assert is_fibonacci(5) == True 
    assert is_fibonacci(2) == True 
    assert is_fibonacci(-1) == False 
    assert is_fibonacci(44444) == False 


# The test Number : 5  
def test_is_Lucas() : 
    assert is_Lucas(123) == True
    assert is_Lucas(0) == False
    assert is_Lucas(9349) == True


# The test Number : 6 
def test_is_triangular() : 
    assert is_triangular( 0 ) == True 
    assert is_triangular( 666 ) == True 
    assert is_triangular( 635 ) == False


# The test Number : 7
def test_is_pronic() : 
    assert is_pronic( 0 ) == True  
    assert is_pronic( 380 ) == True  
    assert is_pronic( 381 ) == False   
    assert is_pronic( 2550 ) == True   
    assert is_pronic(  2551 ) == False   

# The test Number : 8 
def test_is_polite( ) : 
    assert is_polite(4) == False   
    assert is_polite( 50 ) ==  True  
    assert is_polite( 31 ) ==  True 
    assert is_polite( 32 ) ==  False 

# The test Number : 9 
def test_is_perfect() : 
    assert is_perfect( 6 ) == True  
    assert is_perfect( 28 ) == True  
    assert is_perfect( 8128 ) == True  
    assert is_perfect( 8000 ) == False 

# The test Number : 10
def test_is_pentatope() : 
    assert is_pentatope(1365) == True 
    assert is_pentatope(1001) == True
    assert is_pentatope(1)  == True  
    assert is_pentatope(71) == False 

# The test Number : 11
def test_is_pentagonal() : 
    assert is_pentagonal( 1 ) == True 
    assert is_pentagonal( 4030 ) == True 
    assert is_pentagonal( 4020 ) == False 

# The test Number : 12
def test_is_octagonal() : 
    assert is_octagonal(936) == True 
    assert is_octagonal(935) == False 
    assert is_octagonal(1) == True 


# The test Number : 13
def test_is_icosahedral() :
    assert is_icosahedral(5083) == True 
    assert is_icosahedral(3036) == True 
    assert is_icosahedral(1) == True 
    assert is_icosahedral(400) == False 

# The test Number : 14
def test_is_harshad() :
    assert is_harshad(200) == True 
    assert is_harshad(1) == True 
    assert is_harshad(192) == True 
    assert is_harshad(130) == False


# The test Number : 15
def test_is_fermat() :
    assert is_fermat( 3 ) == True 
    assert is_fermat( 5 ) == True 
    assert is_fermat( 17 ) == True 
    assert is_fermat( 4294967297 ) == True 
    assert is_fermat( 4194967291 ) == False


# The test Number : 16 
def test_is_even() : 
    assert is_even( 0 ) == True 
    assert is_even( 90000000 ) == True 
    assert is_even( 21921291981983 ) == False 
    assert is_even( 1 ) == False 


# The test Number : 17 
def test_is_deficient() : 
    assert is_deficient( 1 ) == True 
    assert is_deficient( 50 ) == True 
    assert is_deficient( 41 ) == True 
    assert is_deficient( 40 ) == False 

# This is The test : 18 
def test_is_cullen() : 
    assert is_cullen( 3 ) == True 
    assert is_cullen( 9 ) == True 
    assert is_cullen( 10241 ) == True 
    assert is_cullen( 2 ) == False 

# This is The test : 19 
def test_is_catalan() : 
    assert is_catalan( 16796 ) == True 
    assert is_catalan( 4862 ) == True 
    assert is_catalan( 1 ) == True 
    assert is_catalan( 10 ) == False 

# This is The test : 20 
def test_is_automorphic() : 
    assert is_automorphic(0) == True 
    assert is_automorphic(1) == True 
    assert is_automorphic(890625) == True 
    assert is_automorphic( 99 ) == False 

# This is The test : 21 
def test_is_sphenic( ) : 
    assert is_sphenic(165) == True 
    assert is_sphenic(30) == True 
    assert is_sphenic(2) == False 
    assert is_sphenic(150) == False 

# This is The test : 22 
def test_sum_of_digits() :
    assert sum_of_digits(10) == 1 
    assert sum_of_digits(11111) == 5
    assert sum_of_digits(9155) == 20



