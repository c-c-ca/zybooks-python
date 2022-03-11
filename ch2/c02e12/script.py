#!/usr/bin/python3

# *first_and_middle_names, last_name = input().split()

# print("{}, {}".format(last_name,
# 	"".join(name[0] + "." for name in first_and_middle_names)))


names = input().split()

last_name = names[-1]
print("{}, ".format(last_name), end="")

first_name = names[0]
first_initial = first_name[0]
print("{}.".format(first_initial), end="")

if len(names) == 3:
	middle_name = names[1]
	middle_initial = middle_name[0]
	print("{}.".format(middle_initial), end="")

print()

	
