import random

names_string = input("names: ")

names = names_string.split(", ")

num_item = len(names)

random_choice = random.randint(0, num_item - 1)

who_will_pay = names[random_choice]

print(who_will_pay + " is going to pay fo the meal today!")