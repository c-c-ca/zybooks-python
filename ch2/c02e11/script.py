#!/usr/bin/python3

phone_number = input()
number_segments = phone_number.split("-")
area_code = number_segments[0]
print('Area code:', area_code)