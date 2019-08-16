#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###### Answers to project Euler

# Problem 1: Multiples of 3 and 5
sum(set(list(range(3,1000,3)) + list(range(5, 1000, 5))))

# Problem 2: Sum of even Fibonacci
def even_fib_sum(n):
    fib_sum = 0
    y = 2
    
    x = [1, 2]
    while y <= n:
        if y % 2 == 0:
            fib_sum += y
        y = sum(x)
        x.append(y)
        x.pop(0)
        
    return fib_sum
    
even_fib_sum(4e6)

# Problem 3: Largest prime factor
def is_prime(n, prime_list = None):
    if prime_list is not None:
        for i in prime_list:
            if n % i == 0:
                return False
    else:
        for i in range(3, int(n^0.5), 2):
            if n % i == 0:
                return False
    return True

def largest_prime_factor(n):
    prime_list = [2]
    largest = (0 if n % 2 !=0 else 2)
    for i in range(3, n, 2):
        if is_prime(i, prime_list):
            prime_list.append(i)
            while n % i == 0:
                largest = i
                n /= i
        if i > n:
            break
                
    return largest if n > 0 else n
            
largest_prime_factor(600851475143)

# Problem 4: Largest palimdrome
def is_palimdrome(n):
    n_str = str(n)
    if n_str[:(len(n_str)//2+1)] == n_str[:-(len(n_str)//2+2):-1]:
        return True
    return False

def largest_palimdrome_multiplied_by_digits(lower, upper, digits):
    for i in range(upper, lower, -1):
        if is_palimdrome(i):
            for j in range(10**(digits-1), 10**digits):
                if i % j == 0 and \
                    i / j >= 10**(digits-1) and \
                    i / j < 10**digits:
                    return i, j, i / j
                
largest_palimdrome_multiplied_by_digits(10**2, 99**2, 2)
largest_palimdrome_multiplied_by_digits(100**2, 999**2, 3)

# Problem 51: Prime digit replacements
## Generate is_prime in bits
from bitarray import bitarray

def gen_prime_bit(max_digits):
    is_prime = bitarray(int(10**max_digits))
    is_prime.setall(True)
    is_prime[:2] = False
    is_prime[4::2] = False
    for i in range(3, len(is_prime), 2):
        if is_prime[i]:
            is_prime[i*2::i] = False
    
    return is_prime

## Replace digits for a single prime
def prime_replace_digits(n, is_prime=is_prime):
    n_str = str(n)
    prime_count = []
    prime_list = []
    for i in range(10):
        if str(i) in n_str:
            prime_count.append(1)
            prime_list.append([n])
            for j in range(i+1, 10):
                replaced_number = int(n_str.replace(str(i), str(j)))
                if is_prime[replaced_number]:
                    prime_count[-1] += 1
                    prime_list[-1].append(replaced_number)
    
    return (prime_count, prime_list)

## Find primes based on number of family members
def find_prime_family(members, is_prime=is_prime):
    for number, curr_prime in enumerate(is_prime):
        if (curr_prime):
            count, other_primes = prime_replace_digits(number, is_prime=is_prime)
            if (max(count) == members):
                return max(count), other_primes[count.index(max(count))]
    return None

is_prime = gen_prime_bit(8)
count, primes = prime_replace_digits(50063, is_prime)
find_prime_family(8, is_prime)
            