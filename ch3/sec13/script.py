#! /usr/bin/python3

import sys

num_cents = int(input())

if num_cents <= 0:
    print("No change")
    sys.exit(0)

coin_cents = [100, 25, 10, 5, 1]
coin_names_singular = ["Dollar", "Quarter", "Dime", "Nickel", "Penny"]
coin_names_plural = ["Dollars", "Quarters", "Dimes", "Nickels", "Pennies"]

for cents_per_coin, singular_coin_name, plural_coin_name in zip(
	coin_cents, coin_names_singular, coin_names_plural):
	
	num_coins = num_cents // cents_per_coin

	if num_coins <= 0: continue

	print(num_coins, singular_coin_name if num_coins == 1 else plural_coin_name)

	num_cents %= cents_per_coin


