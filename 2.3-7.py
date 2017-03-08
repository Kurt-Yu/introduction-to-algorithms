#!/usr/bin/env python
# -*-coding:utf-8 -*-
# 2.3-7
'''First we sort S. Afterwards, we iterate it and for each element i 
we perform a binary search to see if there is an element equal to x−i. 
If one is found, the algorithm returns true. Otherwise, it returns false.

We iterate n elements and perform binary search for each on in an n-sized array,
which leads to Θ(nlgn)-time. If we sort first (with merge sort) it will introduce another Θ(nlgn) time, 
that would change the constant in the final algorithm, but not the asymptotic time.
'''


def merge_sort(A):
	if len(A) > 1:
		mid = len(A)//2
		L = A[:mid]
		R = A[mid:]

		merge_sort(L)
		merge_sort(R)

		i = 0
		j = 0
		k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				A[k] = L[i]
				i = i + 1
			else:
			    A[k] = R[j]
			    j = j + 1
			k = k + 1

		while i < len(L):
		    A[k] = L[i]
		    i = i + 1
		    k = k + 1

		while j < len(R):
			A[k] = R[j]
			j = j + 1
			k = k + 1

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


def search(A, x):
	merge_sort(A)
	for i in range(len(A)):
		if binary_search(A, x - A[i]) != None:
			return True
	return False		



A = [3, 41, 52, 26, 38, 57, 9, 49]
print (search(A, 51))



