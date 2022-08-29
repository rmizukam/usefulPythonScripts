def changeVars(userInput):
    Answered = False
    while not Answered:
        if userInput.lower() == 'y':
            userInput = True
            Answered = True
        elif userInput.lower() == 'n':
            userInput = False
            Answered = True
        else:
            userInput = input('Invalid Answer Input (y/n): ')
    return userInput