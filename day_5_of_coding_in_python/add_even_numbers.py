target = int(input("Enter a number: "))

sum_even = 0
for num in range(1, target + 1):
    if target <= 1000:
        if num % 2 == 0:
            sum_even += num
print(sum_even)