#! /usr/bin/python3

base_char = input()
head_char = input()

BASE_WIDTH = 6
EMPTY_CHAR = ' '

EMPTY_BASE = EMPTY_CHAR * BASE_WIDTH
ARROW_BASE = base_char * BASE_WIDTH

row1 = EMPTY_BASE + head_char
row2 = ARROW_BASE + head_char * 2
row3 = ARROW_BASE + head_char * 3
row4 = ARROW_BASE + head_char * 2
row5 = EMPTY_BASE + head_char

print(row1)
print(row2)
print(row3)
print(row4)
print(row5)

print()

print("      " + head_char)
print(base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char)
print(base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char + head_char)
print(base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char)
print("      " + head_char)