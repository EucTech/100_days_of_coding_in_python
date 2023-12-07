#!/usr/bin/python3

"""BMI CALCULATOR that calculates the weight and the height of a person"""

height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

bmi_as_int = int(bmi)
print(bmi_as_int)
