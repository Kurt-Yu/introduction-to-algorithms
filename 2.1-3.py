'''Exercises 2.1-3'''

def return_index(A, v):
	for index in range(0, len(A)):
		if A[index] == v :
		    return index

A = [4, 6, 2, 7, 9]
print (return_index(A, 5))
