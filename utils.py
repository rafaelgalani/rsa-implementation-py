import random as _r
import primes as _p

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
    lower_range = 3
    print(lower_range, totient)
    e = _p.generate(lower_range, totient)
    while not _are_coprimes(e, totient):
        e = _p.generate(lower_range, totient)

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