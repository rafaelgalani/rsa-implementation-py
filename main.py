import rsa

def len_in_bits(x):
	return len(bin(abs(x))[2:])

print('Bits => ', len_in_bits(rsa.p))
print('Bits => ', len_in_bits(rsa.q))
print('Bits => ', len_in_bits(rsa.n))

word = input('Choose a word: ')

print('Word encrypted: {}'.format(
    rsa.encrypt(word)
))

values = input('Send an array: ').split(', ')
values = list(map(int, values))

print('Word decrypted: {}'.format(
    rsa.decrypt(values)
))