#!/usr/bin/env python
# -*-coding: utf-8 -*-
#2.3-5 binary search

def binary_search(A, v):
	low = 0
	high = len(A) - 1
	while low <= high:
		mid = (low + high)//2
		if A[mid] == v:
			return mid
		elif A[mid] < v:
		    low += 1
		else:
		    high -= 1
	return None
	
A = [1, 2, 3, 4, 5]
print (binary_search(A, 1))
print (binary_search(A, 5))        	