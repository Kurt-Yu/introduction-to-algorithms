'''find maximum subarray using divide-and-conquer'''
#!/sur/bin/env python
# -*- coding: utf-8 -*-

def cross_max(A, low, mid, high):
	left_sum = -100
	total_sum = 0
	for i in range(mid, low):
		total_sum += A[i]
		if total_sum > left_sum:
			left_sum = total_sum
			max_left = i

	right_sum = -100
	total_sum = 0
	for j in range(mid+1, high ):
	    total_sum = A[j]
	    if total_sum > right_sum:
	        right_sum = total_sum
	        max_right = j
	return max_left, max_right, left_sum+right_sum        


def max_subarray(A, low, high):
	if high == low:
		return low, high, A[low]
	else:
	    mid = (low + high)//2
	    left_low, left_high, left_sum = max_subarray(A, low, high)
	    right_low, right_high, right_sum = max_subarray(A, low, high)
	    cross_low, corss_high, cross_sum = cross_max(A, low, mid, high)

	    if left_sum > right_sum and left_sum > cross_sum:
	        return left_low, left_high, left_sum
	    elif right_sum > left_sum and right_sum > cross_sum:
	        return right_low, right_high, right_sum
	    else:
	        return cross_low, corss_high, cross_sum            

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print (max_subarray(A, 0, len(A)))

	        		

