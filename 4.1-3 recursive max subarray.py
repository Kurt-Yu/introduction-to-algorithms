#!/sur/bin/env python
# -*-coding: utf-8 -*-
# 4.1-3 recursive algorithm to find max subarray

def crossing(A, low, mid, high):
	left_sum = -1000
	total_sum = 0

	for i in range(mid, low-1, -1):
		total_sum += A[i]
		if total_sum > left_sum:
			left_sum = total_sum
			max_left = i

	right_sum = -1000
	total_sum = 0

	for j in range(mid+1, high+1):
	    total_sum += A[j]
	    if total_sum > right_sum:
	        right_sum = total_sum
	        max_right = j
	return (max_left, max_right, left_sum+right_sum)
	
def max_subarray(A, low, high):
    if high == low:
        return low, high, A[low]

    else:
        mid = (low + high) // 2 

        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, rigth_high, right_sum = max_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = crossing(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
        	return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, rigth_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

A = [20, -21, 43, -23, -92, 45, -56, -5, 34, -17,
                    34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49, 
                    3, -45, 34, 76, 32, -76, -2, 3, -45, 44, 34, 67, 
                    -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34, 
                    88, 56, -6, -89, -90, -34, -56, 23, 29, 2, 6, 9, 
                    2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55, 
                    23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56, 
                    -34, 45, 32, 20, -87, 39, 82, 95, -67, -45, 88, 
                    -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76]
print (max_subarray(A, 0, len(A)-1))               
	
