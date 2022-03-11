#! /usr/bin/python3

def exact_change(user_total):
	coin_amounts = [100, 25, 10, 5, 1]
	change = []

	for amount in coin_amounts:
		change.append(user_total // amount)
		user_total %= amount

	return tuple(change)


if __name__ == "__main__":
	input_val = int(input())
	
	coin_names_singular = ["dollar", "quarter", "dime", "nickel", "penny"]
	coin_names_plural = ["dollars", "quarters", "dimes", "nickels", "pennies"]

	noChange = True
	for num, singular, plural in zip(exact_change(input_val), coin_names_singular, coin_names_plural):
		if num > 0:
			print(num, singular if num == 1 else plural)
			noChange = False

	if noChange:
		print("no change")