def choice_for_sync():
    answered = False
    while not answered:
        userInput = input(
        'Choose option\n'
        '0: Difference Checker\n'
        '1: Source = Cloud, Destination = Local\n'
        '2: Source = Local, Destination = Cloud\n'
        'Selection: '
        )
        if userInput == '0' or userInput == '1' or userInput == '2':
            answered = True
        else:
            print('invalid selection\n'
            '----------------------------------------------------------------------'
            )
    print('----------------------------------------------------------------------')
    return userInput
