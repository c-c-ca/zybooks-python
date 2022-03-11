#! /usr/bin/python3

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

print('%0.2f %0.2f %0.2f' % (
    10 / miles_per_gallon * dollars_per_gallon,
    50 / miles_per_gallon * dollars_per_gallon,
    400 / miles_per_gallon * dollars_per_gallon,
    ))
