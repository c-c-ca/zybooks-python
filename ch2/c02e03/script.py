#! /usr/bin/python3

car_makers = {'Acura': 'Japan', 'Fiat': 'Egypt'}

# Add the key Tesla with value USA to car_makers
car_makers['Tesla'] = 'USA'

# Modify the car maker of Fiat to Italy
car_makers['Fiat'] = 'Italy'

print('Acura made in', car_makers['Acura'])
print('Fiat made in', car_makers['Fiat'])
print('Tesla made in', car_makers['Tesla'])