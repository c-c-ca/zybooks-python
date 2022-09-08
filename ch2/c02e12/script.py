#!/usr/bin/python3

# *first_and_middle_names, last_name = input().split()

# print("{}, {}".format(last_name,
# 	"".join(name[0] + "." for name in first_and_middle_names)))


full_name = input()
names = full_name.split()
	
if len(names) == 3: # there is a middle name
	first_name, middle_name, last_name = names
	print("{}, {}.{}.".format(last_name, first_name[0], middle_name[0]))
else: # there is no middle name
	first_name, last_name = names
	print("{}, {}.".format(last_name, first_name[0]))