"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    list = []
    x = 2
    how_many = 0
    
    while how_many != number_of_primes:
        
        if prime_or_not(x):
            list.append(x)
            x += 1
            how_many=how_many+1
            
        else:
            x += 1
         

    return list
    
def prime_or_not(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True
        
