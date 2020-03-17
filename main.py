from rsa import RSA
from utils import *
from primes import is_prime

sections = {
   
    "action": {
        "valids": ("1", "2", "3"),
        "message": 'Choose an action:\n1 - Encrypt\n2 - Decrypt\n3 - Quit\n\n'
    },
    
    "values_origin": {
        "valids": ("1", "2", "3"),
        "message": 'Do you want to use your own values?\n1 - Yes\n2 - No\n3 - Quit\n\n'
    },
    
    "show_values": {
        "valids": ("1", "2"),
        "message": 'Do you want to see the values of the RSA instance?\n1 - Yes\n2 - No\n\n'
    },
    
    "continue_with_instance": {
        "valids": ("1", "2"),
        "message": 'Do you want to keep using this instance?\n1 - Yes\n2 - No\n\n'
    },
}

def input_section(section_entry):
    option = input(section_entry["message"])

    while option not in section_entry["valids"]:
        print(section_entry["valids"])
        print('Option "{}" is invalid.'.format(option))
        option = input(section_entry["message"])

    return option

def is_e_valid(p, q, e):
    totient = (p-1)*(q-1)
    if e >= totient:
        return False
    elif are_coprimes(e, totient) and is_prime(e):
        return True
    return False

def get_init_value_input(message, first_value=None):
    while True:
        try:
            value = int(input(message))
            invalid_value = type(first_value) == int and first_value == value

            while not RSA.is_prime(value) or value <= 2 or invalid_value:
                
                if not RSA.is_prime(value):
                    print('The chosen value "{}" is not prime. Try another one.'.format(value))
                elif value <= 2:
                    print('The value must be greater than 2. Try another one.')
                elif invalid_value:
                    print('The chosen value must be different than the previous one. Try another one.')

                value = int(input(message))
                invalid_value = type(first_value) == int and first_value == value
                
            return value
        except ValueError:
            print('The value typed is not a valid number. Try another one.')

def get_e_value(message):
    while True:
        try:
            value = int(input(message))
            e_valid = is_e_valid(p, q, value)
            value_lte_2 = value <= 2

            while not e_valid or value_lte_2:
                if not e_valid:
                    print('The chosen value "{}" is not valid (must be lower than totient, coprime with totient and also a prime number). Try another one.'.format(value))
                elif value_lte_2:
                    print('The value must be greater than 2. Try another one.')

                value = int(input(message))
                e_valid = is_e_valid(p, q, value)
                value_lte_2 = value <= 2
            return value
        except ValueError:
            print('The value typed is not a valid number. Try another one.')


def ask_input(name):
    return input_section(sections[name])


run = True

while run:
    print()
    use_own_values = ask_input("values_origin")

    if use_own_values == "1":
        print()
        print('Setting values up...')
        p = get_init_value_input('P: ')
        q = get_init_value_input('Q: ', p)
        e = get_e_value('E: ')
        print()
        
        rsa = RSA(p, q, e)
    elif use_own_values == "2":
        rsa = RSA.get_random_rsa()
    elif use_own_values == "3":
        run = False
        break
    
    show_values = ask_input("show_values")

    if show_values == "1":
        rsa.show_values()

    continue_with_instance = "1"

    while continue_with_instance == "1":
        print()
        action = ask_input("action")
        print()

        if action == "1":
            word = input('Choose a word: ')
            print('Word encrypted: {}'.format(
                rsa.encrypt(word)
            ))

        elif action == "2":
            values = input('Input the word encrypted values: ')
            values = list(map(int, values.split(', ')))

            print('Word decrypted: {}'.format(
                rsa.decrypt(values)
            ))

        continue_with_instance = ask_input("continue_with_instance")
        run = continue_with_instance != "3"