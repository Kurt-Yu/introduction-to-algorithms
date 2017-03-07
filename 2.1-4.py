'''2.1-4'''

def add_two_binary_numbers(a, b):
	return bin(int(a, 2) + int(b, 2))
	
a = '10010'
b = '10110'
print (add_two_binary_numbers(a, b))