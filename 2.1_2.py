'''Insertion Sort in Python'''
'''Exercises 2.1-2'''

def insertionSort(A):
   for index in range(1,len(A)):

     key = A[index]
     position = index

     while position>0 and A[position-1] < key:
         A[position] = A[position-1]
         position = position-1
     A[position] = key

A = [54,26,93,17,77,31,44,55,20]
insertionSort(A)
print (A)