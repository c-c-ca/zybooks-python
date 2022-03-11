#! /usr/bin/python3

while True:
	item, count = input().split()
	if item == "quit": break
	print("Eating {} {} a day keeps the doctor away.".format(count, item))