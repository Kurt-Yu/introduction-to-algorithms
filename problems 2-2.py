# problems 2-2  Correctness of bubblesort
#!/usr/bin/env python
# -*-coding:utf-8 -*-

def bubblesort(A):
	flag = True
	while flag == True:
		flag = False
		for i in range(len(A)-1):
			if A[i] > A[i+1]:
			    temp = A[i]
			    A[i] = A[i+1]
			    A[i+1] = temp
			    flag = True
		


A = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
bubblesort(A)
print (A)
