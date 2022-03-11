#!/usr/bin/python3

from math import pow, sqrt

x = float(input())
y = float(input())
z = float(input())

print("{:.2f} {:.2f} {:.2f} {:.2f}".format(
	pow(x, z),
	pow(x, pow(y, z)),
	abs(x - y),
	sqrt(pow(x, z))
))