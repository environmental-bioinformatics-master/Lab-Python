#!/usr/bin/env python3

def factorial(num):
	# Calculates factorial for a number
	factorial_num = 1
	if num < 0:
		print("Sorry, factorial does not exist for negative numbers")
	elif num==0:
		print("The factorial of 0 is 1")
	else:
		for i in range(1, num + 1):
			factorial_num = factorial_num * i
		print("The factorial of", num, "is", factorial_num)

if __name__ == "__main__": 

	num = int(input("Enter a number: "))
	factorial(num)
