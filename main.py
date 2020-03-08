from rsa import RSA

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

def get_init_value_input(message):
    while True:
        try:
            value = int(input(message))
            while not RSA.is_prime(value) or value <= 2:
                
                if not RSA.is_prime(value):
                    print('The chosen value "{}" is not prime. Try another one.'.format(value))
                if value <= 2:
                    print('The value must be greater than 2. Try another one.')

                value = int(input(message))
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
        q = get_init_value_input('Q: ')
        print()
        
        rsa = RSA(p, q)
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