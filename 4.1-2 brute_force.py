# brute_force to find max subarray in python
#!/usr/bin/env python
# -*-coding: utf-8 -*-

def max_subarray(A):
	result = 0
	for i in range(len(A)):
		temp = 0
		for j in range(i, len(A)):
			temp += A[j]
			if temp > result:
				result = temp
				left = i
				right = j

	return left, right, result
	
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]	
print (max_subarray(A))

# time complexity: O(n^2)
