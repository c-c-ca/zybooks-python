#!/usr/bin/python3

user_int = int(input('Enter integer (32 - 126):\n'))
# print(user_int)

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = input('Enter float:\n')
# print(user_float)

user_chr = input('Enter character:\n')
# print(user_chr)

user_str = input('Enter string:\n')
# print(user_str)
                         
print(user_int, user_float, user_chr, user_str)

# FIXME (2): Output the four values in reverse
 
print(user_str, user_chr, user_float, user_int)               
               
# FIXME (3): Convert the integer to a characer, and output that character

print(user_int, 'converted to a character is', chr(user_int))