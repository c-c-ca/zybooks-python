#!/usr/bin/python3

standard_cups_of_lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
standard_cups_of_water = float(input('Enter amount of water (in cups):\n'))
standard_cups_of_agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
standard_num_servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(standard_num_servings))
print('{:.2f} cup(s) lemon juice'.format(standard_cups_of_lemon_juice))
print('{:.2f} cup(s) water'.format(standard_cups_of_water))
print('{:.2f} cup(s) agave nectar'.format(standard_cups_of_agave_nectar))

desired_num_servings = float(input('\nHow many servings would you like to make?\n'))
standard_to_desired =  desired_num_servings / standard_num_servings
desired_cups_of_lemon_juice = standard_cups_of_lemon_juice * standard_to_desired
desired_cups_of_water = standard_cups_of_water * standard_to_desired
desired_cups_of_agave_nectar = standard_cups_of_agave_nectar * standard_to_desired

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_num_servings))
print('{:.2f} cup(s) lemon juice'.format(desired_cups_of_lemon_juice))
print('{:.2f} cup(s) water'.format(desired_cups_of_water))
print('{:.2f} cup(s) agave nectar'.format(desired_cups_of_agave_nectar))

desired_gallons_of_lemon_juice = desired_cups_of_lemon_juice / 16.0
desired_gallons_of_water = desired_cups_of_water / 16.0
desired_gallons_of_agave_nectar = desired_cups_of_agave_nectar / 16.0

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_num_servings))
print('{:.2f} gallon(s) lemon juice'.format(desired_gallons_of_lemon_juice))
print('{:.2f} gallon(s) water'.format(desired_gallons_of_water))
print('{:.2f} gallon(s) agave nectar'.format(desired_gallons_of_agave_nectar))