import database

class User(object):
    """Docstring"""
    
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = self.create_password()
        self.receipts = []
        
    def __str__(self):
        return ''.join([self.first_name, ' ', self.last_name, 
                        ' (', self.username, ')'])
    
    def add_receipt(self, receipt):
        """
        Adds a receipt object to the user
        """
        self.items.append(receipt)
    
    def create_password(self):
        first_entry = ''
        second_entry = '#'
        
        while first_entry != second_entry:
            print("For security purposes, please enter a password?")
            first_entry = raw_input('> ')
            print("Could you confirm that for me?")
            second_entry = raw_input('> ')
            
            if first_entry != second_entry:
                print("Sorry, those passwords don't match. Can you try again.")
        
        return first_entry