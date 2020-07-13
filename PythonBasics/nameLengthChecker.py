name = 'Robert'
char_count = len(name)

if char_count < 3:
    print('name must be at least 3 characters')
elif char_count > 50:
    print('name can be maximum of 50 characters')
else:
    print('name looks good')

