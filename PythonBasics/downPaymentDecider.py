has_good_credit = True
house_price = 1000000

if has_good_credit:
    down_payment = house_price * 0.1

else:
    down_payment = house_price * 0.2

print(f'Down payment owed is ${int(down_payment)}')
