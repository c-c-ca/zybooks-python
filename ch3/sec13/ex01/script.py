#! /usr/bin/python3

phone_number = int(input())

line_number = phone_number % 10000
phone_number //= 10000
prefix = phone_number % 1000
phone_number //= 1000
area_code = phone_number % 1000
phone_number //=1000

print(f'({area_code}) {prefix}-{line_number}')