#! /usr/bin/python3

def number_of_pennies(num_dollars, num_pennies=0):
	return num_dollars * 100 + num_pennies

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))              # Dollars only!