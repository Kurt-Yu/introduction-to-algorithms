'''2.3-1 Merge Sort in python'''

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

A = [3, 41, 52, 26, 38, 57, 9, 49]
merge_sort(A)
print (A)	    	
      
