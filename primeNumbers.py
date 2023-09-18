# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:21:36 2023

@author: arnulfomartinez

Find prime numbers between a set of numbers

"""

def find_primes(upper_limit=100):
    number_range = set(range(2, upper_limit + 1))
    prime_numbers = []
    while number_range:
        prime = number_range.pop()
        prime_numbers.append(prime)
        multiples = set(range(prime*2, upper_limit+1, prime))    
        number_range.difference_update(multiples)
        
    return prime_numbers




upper_limit = 10000000
primes = find_primes(upper_limit)
prime_count = len(primes)

largest_prime = max(primes)

print(f"There are {prime_count} prime numbers between 2 and {upper_limit}, the largest of which is {largest_prime}")
