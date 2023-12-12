import random
import string

numbers = string.digits
letters = string.ascii_letters
symbols = string.punctuation

numbers_input = int(input("How many numbers would you like in your password? "))
letter_input = int(input("How many letters would you like? "))
symbols_input = int(input("How many symbols would you like? "))

random_number = random.choices(numbers, k=numbers_input)
random_letters = random.choices(letters, k=letter_input)
random_symbols = random.choices(symbols, k=symbols_input)
random_password_list = []
random_password_list.extend(random_number)
random_password_list.extend(random_letters)
random_password_list.extend(random_symbols)

random_password_str = ''
for password in random_password_list:
    random_password_str += str(password)
print(random_password_str)


