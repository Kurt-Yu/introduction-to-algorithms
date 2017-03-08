'''Fibonacci numbers using Golden Ratio'''
#!/sur/bin/env python
# -*- coding: utf-8 -*-

def power(x, n):
	if n == 1:
		return x
	else:
	    return x*power(x, n-1)	

def Fibonacci(n):
	return round((power((1 + 5**0.5)/2, n) - power((1 - 5**0.5)/2, n)) / (5**0.5))

print(Fibonacci(70))	

#前70项是精确的
	