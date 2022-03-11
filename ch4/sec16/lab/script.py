#! /usr/bin/python3

import sys

highway_number = int(input())

primary_highway_number = highway_number % 100

if primary_highway_number <= 0:
	print("{} is not a valid interstate highway number.".format(highway_number))
	sys.exit(0)

print("I-{} is ".format(highway_number), end="")
if highway_number < 100:
	print("primary", end="")
else:
	print("auxiliary, serving I-{}".format(primary_highway_number), end="")

print(", going ", end="")
if highway_number % 2 == 0:
	print("east/west", end="")
else:
	print("north/south", end="")
print(".")


