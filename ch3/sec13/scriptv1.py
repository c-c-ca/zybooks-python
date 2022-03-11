#! /usr/bin/python3

CENTS_PER_DOLLAR = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

num_cents = int(input())

if num_cents <= 0:
	print('No change')

num_dollars = num_cents // CENTS_PER_DOLLAR
num_cents %= CENTS_PER_DOLLAR

if num_dollars == 1:
	print(num_dollars, 'Dollar')
elif num_dollars > 1:
	print(num_dollars, 'Dollars')

num_quarters = num_cents // CENTS_PER_QUARTER
num_cents %= CENTS_PER_QUARTER

if num_quarters == 1:
	print(num_quarters, 'Quarter')
elif num_quarters > 1:
	print(num_quarters, 'Quarters')

num_dimes = num_cents // CENTS_PER_DIME
num_cents %= CENTS_PER_DIME

if num_dimes == 1:
	print(num_dimes, 'Dime')
elif num_dimes > 1:
	print(num_dimes, 'Dimes')

num_nickels = num_cents // CENTS_PER_NICKEL
num_cents %= CENTS_PER_NICKEL

if num_nickels == 1:
	print(num_nickels, 'Nickel')
elif num_nickels > 1:
	print(num_nickels, 'Nickels')

if num_cents == 1:
	print(num_cents, 'Penny')
elif num_cents > 1:
	print(num_cents, 'Pennies')
	