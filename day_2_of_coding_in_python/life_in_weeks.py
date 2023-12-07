#!/usr/bin/python3

weeks_in_one_month = 52
months_in_one_year = 12
weeks_in_one_year = weeks_in_one_month * months_in_one_year

lived_up_to_90_years = weeks_in_one_year * 90

current_age = int(input("Your age "))

current_age_in_weeks = current_age * weeks_in_one_year

To_get_weeks_left = lived_up_to_90_years - current_age_in_weeks

print(To_get_weeks_left)
