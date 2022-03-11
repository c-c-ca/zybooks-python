#! /usr/bin/python3

import math

def find_hypotenuse(a, b):
	return math.sqrt(a * a + b * b)


if __name__ == "__main__":
	a = float(input())
	b = float(input())

	hypotenuse = find_hypotenuse(a, b)

	print("{:.2f}".format(hypotenuse))