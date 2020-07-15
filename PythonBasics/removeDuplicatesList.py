numbers = [2, 3, 7, 3, 7, 9]
duplicates_removed = []

for num in numbers:
    if num not in duplicates_removed:
        duplicates_removed.append(num)

print( duplicates_removed)
