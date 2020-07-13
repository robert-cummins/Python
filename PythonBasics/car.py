car_started = False
quit = False

while not quit:
    command = input('Enter a command or type help ').upper()
    if command == 'HELP':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - exit')

    elif command == 'START':
        if not car_started:
            car_started = True
            print("The car has been started")
        else:
            print("The car is already running")

    elif command == 'STOP':
        if car_started:
            car_started = False
            print('The car has been turned off')
        else:
            print('The car has already been turned off')

    elif command == 'QUIT':
        quit = True

    else:
        print("I don't understand that command")
