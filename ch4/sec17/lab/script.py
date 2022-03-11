#! /usr/bin/python3

QUIT = "quit"
MADLIB_FMT = "Eating {} {} a day keeps the doctor away."

while True:
	item, count = input().split()
	if item == QUIT:
		break
	print(MADLIB_FMT.format(count, item))