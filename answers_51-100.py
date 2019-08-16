#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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