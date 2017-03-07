'''2.2-2    Selection Sort'''
# -*- coding: utf-8 -*-

def Selection_sort(A):
	for i in range(len(A)):                 #重复（元素个数－1）次
		smallest = i                        #  把第一个没有排过序的元素设置为最小值
		for j in range(i+1, len(A)):        #  历遍每个没有排过序的元素
			if A[j] < A[smallest]:          #    如果元素 < 现在的最小值
				smallest = j                #      set element as new minmun
		temp = A[i]		                    #  将最小值的第一个没有排序过的位置交换
		A[i] = A[smallest]
		A[smallest] = temp


A = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
Selection_sort(A)
print (A)

