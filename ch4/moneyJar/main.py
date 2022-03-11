#! /usr/bin/python3

num_quarters = int(input())
num_dimes = int(input())
num_nickels = int(input())
num_pennies = int(input())

dollars_for_quarters = num_quarters * 25 / 100
print("{} quarters is ${:.2f}".format(num_quarters, dollars_for_quarters))

dollars_for_dimes = num_dimes * 10 / 100
print("{} dimes is ${:.2f}".format(num_dimes, dollars_for_dimes))

dollars_for_nickels = num_nickels * 5 / 100
print("{} nickels is ${:.2f}".format(num_nickels, dollars_for_nickels))

dollars_for_pennies = num_pennies / 100
print("{} pennies is ${:.2f}".format(num_pennies, dollars_for_pennies))

total_dollars = dollars_for_quarters + dollars_for_dimes + dollars_for_nickels + dollars_for_pennies
print("\nThe total amount of money in the jar is ${:.2f}.".format(total_dollars))