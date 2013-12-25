def ask_yes_no_question():
    """Asks the user to answer yes or no, returns a boolean"""
    while True:
        answer = raw_input('Yes or No? ')
        
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        if answer.lower() == 'no' or  answer.lower() == 'n':
            return False