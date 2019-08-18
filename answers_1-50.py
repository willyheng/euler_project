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

# Problem 5: Smallest multiple
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

def prime_factorise(n, prime_bit=prime_bit):
    prime_factors = {}
    for prime, is_prime in enumerate(prime_bit):
        if is_prime and n % prime == 0:
            prime_factors[prime] = 1
            n /= prime
            while (n % prime == 0):
                prime_factors[prime] += 1
                n /= prime
        if n == 1:
            break
    return prime_factors
            
def lcm(a, b):
    a_factors = prime_factorise(a)
    b_factors = prime_factorise(b)
    
    lcm = 1
    for prime in a_factors:
        if prime in b_factors.keys():
            lcm *= prime ** max(a_factors[prime], b_factors[prime])
            del(b_factors[prime])
        else:
            lcm *= prime ** a_factors[prime]
        
    for prime in b_factors:
        lcm *= prime ** b_factors[prime]
    
    return lcm

prime_bit = gen_prime_bit(5)

x = 1
for i in range(1, 21):
    x = lcm(x, i)
print(x)

# Problem 6: Sum square difference
def sum_square(n):
    return sum([x**2 for x in range(1,n+1)])
def square_sum(n):
    return sum(list(range(1,n+1)))**2
def diff_squares(n):
    return abs(sum_square(n) - square_sum(n))

diff_squares(10)
diff_squares(100)

# Problem 7: 10001st prime
def prime_bit_to_list(prime_bit):
    return [n for n, is_prime in enumerate(prime_bit) if is_prime]

is_prime = gen_prime_bit(8)
prime_list = prime_bit_to_list(is_prime)
prime_list[10000]

# Problem 8: Largest product in series
def largest_adj_product(n_str, n_digits):
    ns = [int(x) for x in n_str]
    max_p = 0
    for i in range(len(n_str) - n_digits + 1):
        p = np.prod(ns[i:(i+n_digits)])
        max_p = max(max_p, p)
    return max_p

x = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace("\n","")

largest_adj_product(x, 13)

# Problem 9: Special pythagorean triplet
def find_pythagorean_triplet(n = 1000):    
    for a in range(1,n):
        for b in range(a+1, n+1):
            if (a + b >= n):
                break
            c = n - a - b
            if c**2 == a**2 + b**2:
                return (a * b * c, (a, b, c))

    return -1

find_pythagorean_triplet()

# Problem 10: Summation of primes
def gen_prime(n_digits):
    prime_bit = gen_prime_bit(n_digits)
    return [n for n, is_prime in enumerate(prime_bit) if is_prime]


primes = np.array(gen_prime(7))
sum(primes[primes < 2e6])

# Problem 11: Largest product in a grid
def product_in_grid(grid, length):
    max_prod = 1
    for i in range(grid.shape[0] - length):
        for j in range(grid.shape[1]):
            right = np.prod(grid[i, j:(j+length)]) if j+length <= grid.shape[1] else -1
            down = np.prod(grid[i:(i+length), j])
            diag_right = np.prod([grid[i+x, j+x] for x in range(length)]) if j+length <= grid.shape[1] else - 1
            diag_left = np.prod([grid[i+x, j-x] for x in range(length)]) if j >= length else -1
            max_prod = max([max_prod, right, down, diag_right, diag_left])
            
    return max_prod
            
inp = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

grid = np.fromstring(inp.replace("\n"," "), dtype=int, sep=' ')
grid = grid.reshape(int(len(grid)**0.5),-1)

product_in_grid(grid, 4)