#!/usr/bin/python3

age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())

calories_woman = ((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184
calories_man = ((age * 0.2017) + (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184

print('Women: {:.2f} calories'.format(calories_woman))
print('Men: {:.2f} calories'.format(calories_man))
