#! /usr/bin/python3

word = input()
password = word

original_str = "iamBo"
replacement_str = "!@M8."

for original, replacement in zip(original_str, replacement_str):
	password = password.replace(original, replacement)
password = password + ('q*s')

print(password)