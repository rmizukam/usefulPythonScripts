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

def choice_for_package():
    answered = False
    while not answered:
        userInput = input(
        'What folder should be synced\n'
        '0: RAW\n'
        '1: dataAFMrm\n'
        '2: cpaAnalysis\n'
        '3: nanoscopeAFM\n'
        '4: SOP-collection\n'
        'Choose selection with number: '
        )
        valid_answers = ['0', '1', '2', '3']
        if userInput in valid_answers:
            answered = True
        else:
            print('invalid selection\n'
            '----------------------------------------------------------------------'
            )
    print('----------------------------------------------------------------------')
    return userInput