numbers = [2, 6, 1, 20, 15, 17, 23, 7, 12]
highest_number = numbers[0]

for num in numbers:
    if num > highest_number:
        highest_number = num

print(highest_number)
