#! /usr/bin/python3

current_price = int(input())
last_months_price = int(input())

''' Type your code here. '''
change_in_price = current_price - last_months_price

print("This house is ${}. The change is ${} since last month.".format(
	current_price, change_in_price))

estimated_monthly_mortgage = (current_price * 0.051) / 12.0

print("The estimated monthly mortgage is ${:.2f}".format(
	estimated_monthly_mortgage))