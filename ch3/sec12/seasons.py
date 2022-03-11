#! /usr/bin/python3

import sys

WINTER = 'Winter'
SPRING = 'Spring'
SUMMER = 'Summer'
AUTUMN = 'Autumn'

ERROR_MSG = 'Invalid'

START_OF_SPRING = 3
START_OF_SUMMER = 6
START_OF_AUTUMN = 9

MARCH = 2
JUNE = 5
SEPTEMBER = 8
DECEMBER = 9

input_month = input()
input_day = int(input())

# Spring: March 20 - June 20 
# Summer: June 21 - September 21 
# Autumn: September 22 - December 20 
# Winter: December 21 - March 19

month_names = [
        'January', 'February', 'March',    # Winter
        'April', 'May', 'June',            # Spring
        'July', 'August', 'September',     # Summer
        'October', 'November', 'December'  # Fall
        ]


month_days = [
        31, # January
        28, # February
        31, # March
        30, # April
        31, # May
        30, # June
        31, # July
        31, # August
        30, # September
        31, # October
        30, # November
        31  # December
        ]


if input_month not in month_names:
        print(ERROR_MSG)
        quit()


month_index = month_names.index(input_month)
days_in_month = month_days[month_index]
if not (1 <= input_day <= days_in_month):
        print(ERROR_MSG)
        quit()


if input_month in month_names[START_OF_SPRING:START_OF_SUMMER]:
        season = SPRING
elif input_month in month_names[START_OF_SUMMER:START_OF_AUTUMN]:
        season = SUMMER
elif input_month in month_names[START_OF_AUTUMN:]:
        season = AUTUMN
else:
        season = WINTER
    
if input_month == month_names[MARCH] and input_day >= 20:
        season = SPRING
elif input_month == month_names[JUNE] and input_day >= 21:
        season = SUMMER
elif input_month == month_names[SEPTEMBER] and input_day >= 22:
        season = AUTUMN
elif input_month == month_names[DECEMBER] and input_day >= 21:
        season = WINTER

print(season)