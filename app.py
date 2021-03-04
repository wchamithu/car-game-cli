started = False
while True:
    command = input('> ').upper()

    if command == 'HELP':
        print('''
                start - Start the car
                stop - Stop the car
                quit - Quit the game
        ''')
    elif command == 'START':
        if not started:
            print('Car started... Ready to go !')
            started = True
        else:
            print('Car alredy started')
    elif command == 'STOP':
        if not started:
            print('Car already stopped')
        else:
            print('Car stopped')
            started = False
    elif command == 'QUIT':
        exit(0)
    else:
        print('I do not understand')