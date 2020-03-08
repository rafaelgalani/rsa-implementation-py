import primes
from utils import *

p,q = primes.generate_list(2)

n = p*q
totient_n = (p-1)*(q-1)
e = generate_e(totient_n)
d = mod_multiplicative_inverse(e, totient_n)

print('p', p)
print('q', q)
print('n', n)
print('totient_n', totient_n)
print('e', e)
print('d', d)

def encrypt_char_function(char_code):
    return pow(char_code, e, n)

def decrypt_value_function(value):
    return pow(value, d, n)

def encrypt(word):
    encrypted_word_arr = []
    for char in word:
        char_code = ord(char)
        encrypted_code = encrypt_char_function(char_code)
        
        encrypted_word_arr.append(encrypted_code)
    
    return encrypted_word_arr

def decrypt(values):
    decrypted_word = ''
    for n in values:

        decrypted_char_code = decrypt_value_function(n)
        
        char_value = chr(decrypted_char_code)
        decrypted_word += char_value
    
    return decrypted_word