#! /usr/bin/python3

num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

'''Your solution goes here'''
for row in range(num_rows):
	for col in range(num_cols):
		print("{}{}".format(row + 1, chr(ord("A") + col)), end=" ")