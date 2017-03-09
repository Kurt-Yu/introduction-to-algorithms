#!/sur/bin/env python
# -*- coding: utf-8 -*-
# 4.1-4 linear time to find max subarray


def max_subarray(A):
	left = 0
	right = 0
	result = A[0]
	temp_sum = 0
	temp_left = 0
	for i in range(len(A)):
		temp_sum = max(A[i], temp_sum + A[i])
		if temp_sum > result :
			result = temp_sum
			right = i
			left = temp_left

		if temp_sum == A[i]:
			temp_left = i

	return left, right, result		

A = [20, -21, 43, -23, -92, 45, -56, -5, 34, -17,
     34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49, 
     3, -45, 34, 76, 32, -76, -2, 3, -45, 44, 34, 67, 
     -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34, 
     88, 56, -6, -89, -90, -34, -56, 23, 29, 2, 6, 9, 
     2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55, 
     23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56, 
     -34, 45, 32, 20, -87, 39, 82, 95, -67, -45, 88, 
     -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76]			

print(max_subarray(A))





