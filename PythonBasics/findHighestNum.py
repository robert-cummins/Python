def find_highest_num(list):
    highest = 0
    for num in list:
        if num > highest:
            highest = num
    print(highest)


