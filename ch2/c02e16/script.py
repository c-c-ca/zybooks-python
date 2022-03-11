#!/usr/bin/python3

NUM_KEYS = 5
r = 2 ** (1 / 12)

f0 = int(input())

print(" ".join("{:.2f}".format(f0 * r ** n) for n in range(NUM_KEYS)))
