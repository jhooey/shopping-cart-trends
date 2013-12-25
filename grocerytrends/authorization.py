from globalmethods import ask_yes_no_question

def login():
    logged_in = False
        
    while not logged_in:
        print("Are you registered?")
        if ask_yes_no_question():    
            logged_in, session_user = check_user()
        else:
            create_user()
            print("Let's restart the login process")
    return session_user
            
def check_user():
    print("What is your username?")
    session_user = session.query(user.User).filter_by(
                                                      username=raw_input('> ')
                                                      ).first() 
    if session_user:
        return check_pwd(session_user), session_user
    else:
        print("Sorry we could not find your username")
        return False, None 

def check_pwd(session_user):
    print("What is your password?")
    input_password = raw_input('> ')
    
    return input_password == session_user.password

def create_user():
    print("What's your first name?")
    first_name = raw_input('> ')
    print("What's your last name?")
    last_name = raw_input('> ')
    print("What do you want as your username?")
    username = raw_input('> ')
    
    session.add(user.User(first_name, last_name, username))
    session.commit()