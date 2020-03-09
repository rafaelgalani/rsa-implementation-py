import random as _r
import primes as _p
import math as _m

def get_bits(x):
	return len(bin(abs(x))[2:])

def _are_coprimes(x, y):
    return _calc_gcd(x, y) == 1

def _calc_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def calc_lcm(x, y):
   lcm_value = (x*y)//_calc_gcd(x, y)
   return lcm_value

def generate_e(totient):
    max_bits_size = _r.randint(2, get_bits(totient)-1)

    max_bits_size = min(75, max_bits_size)

    e = _p.generate_prime_number(max_bits_size)
    
    while not _are_coprimes(e, totient):
        e = _p.generate_prime_number(max_bits_size)

    return e

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def mod_multiplicative_inverse(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m