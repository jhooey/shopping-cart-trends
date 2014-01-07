from globalmethods import ask_yes_no_question
import Tkinter as tk
import user

TITLE_FONT = ("Helvetica", 18, "bold")

class Authorzation(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, Register):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="Shopping Cart Trends", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        
        label_username = tk.Label(self, text="username")
        label_username.pack()
        self.username = tk.StringVar()
        tk.Entry(self, textvariable=self.username).pack()
        
        label_password = tk.Label(self, text="password")
        label_password.pack()
        self.password = tk.StringVar()
        tk.Entry(self, textvariable=self.password).pack()
        
        
        login_btn = tk.Button(self, text="Login", 
                            command=lambda: controller.show_frame(Login))
        login_btn.pack(pady=5)
        
        reg_btn = tk.Button(self, text="Registration", 
                            command=lambda: controller.show_frame(Register))
        reg_btn.pack(pady=10)
        
        
        """Checks if a user exists and is logged in
        logged_in = False
            
        while not logged_in:
            print("Are you registered?")
            if ask_yes_no_question():    
                logged_in, session_user = check_user(session)
            else:
                create_user(session)
                print("Let's restart the login process")
        return session_user"""
    
class Register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", 
                           command=lambda: controller.show_frame(Login))
        button.pack()
    
    
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