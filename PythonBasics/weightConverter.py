weight = input('What is your weight? ')
weight_type = input('Is that (l)bs or (K)Gs ')
convert_to_kg = int(weight) / 2.2
convert_to_pounds = int(weight) * 2.2

if weight_type.upper() == 'L':
    print('Your weight in KGs is ' + str(convert_to_kg))
elif weight_type.upper() == 'K':
    print('Your weight in lbs is ' + str(convert_to_pounds))

