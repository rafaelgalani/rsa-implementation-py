import primes
from utils import *

class RSA:

    @staticmethod
    def is_prime(n):
        return primes.is_prime(n)
    
    def __init__(self, p, q):
        self.p = p
        self.q = q

        self.n         = n         = p*q
        self.totient_n = totient_n = (p-1)*(q-1)
        self.e         = e         = generate_e(totient_n)
        self.d         = d         = mod_multiplicative_inverse(e, totient_n)

    def encrypt_char_function(self, char_code):
        return pow(char_code, self.e, self.n)

    def decrypt_value_function(self, value):
        return pow(value, self.d, self.n) 

    def encrypt(self, word):
        encrypted_word_arr = []
        for char in word:
            char_code = ord(char)
            encrypted_code = self.encrypt_char_function(char_code)
            
            encrypted_word_arr.append(encrypted_code)
        
        return encrypted_word_arr

    def decrypt(self, values):
        decrypted_word = ''
        for n in values:

            decrypted_char_code = self.decrypt_value_function(n)
            
            char_value = chr(decrypted_char_code)
            decrypted_word += char_value
        
        return decrypted_word

    @staticmethod
    def get_random_rsa():
        p, q = primes.generate_prime_number(2048), primes.generate_prime_number(2048)

        return RSA(p, q)

    def show_values(self):
        print()
        print('Values used in this instance:')
        print()
        print('P         => ', self.p)
        print('Q         => ', self.q)
        print('N         => ', self.n)
        print('TOTIENT_N => ', self.totient_n)
        print('E         => ', self.e)
        print('D         => ', self.d)

        print('P bits    => ', get_bits(self.p))
        print('Q bits    => ', get_bits(self.q))
        print('N bits    => ', get_bits(self.n))
        print()