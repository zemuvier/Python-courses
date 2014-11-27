# -*- coding: cp1251 -*-

def fib(n): #нерекурсивный алгоритм

	fib1 = fib2 = 1
	i = 2

	while i < n:
		fibs = fib1 + fib2
		fib1 = fib2
		fib2 = fibs
		i = i + 1

	print fibs;
