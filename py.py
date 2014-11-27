# -*- coding: cp1251 -*-

def fib(n): #рекурсивный алгоритм

	if n <= 0:
		print 0

	elif n == 1 or n == 2:
		print 1

	else:
		print fib(n-1) + fib(n-2);