from globalmethods import ask_yes_no_question
import user

def login(session):
    """Checks if a user exists and is logged in"""
    logged_in = False
        
    while not logged_in:
        print("Are you registered?")
        if ask_yes_no_question():    
            logged_in, session_user = check_user(session)
        else:
            create_user(session)
            print("Let's restart the login process")
    return session_user
            
def check_user(session):
    """Checks to see if the username can be found in the database"""
    print("What is your username?")
    session_user = session.query(user.User).filter_by(
                                                      username=raw_input('> ')
                                                      ).first() 
    if session_user:
        return session_user.check_pwd(), session_user
    else:
        print("Sorry we could not find your username")
        return False, None 

def create_user(session):
    """Gathers the info necessary to create a new user"""
    print("What's your first name?")
    first_name = raw_input('> ')
    print("What's your last name?")
    last_name = raw_input('> ')
    print("What do you want as your username?")
    username = raw_input('> ')
    
    session.add(user.User(first_name, last_name, username))
    session.commit()