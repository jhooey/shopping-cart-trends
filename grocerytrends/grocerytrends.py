import receipt
import user

print("Welcome! Shall we dive in and judge your spending habits?")
print("We can start by figuring out who's here.")
print("What's your first name?")
first_name = raw_input('> ')
print("What's your last name?")
last_name = raw_input('> ')
print("What do you want as your username?")
username = raw_input('> ')

password = user.create_password()

user1 = user.User(first_name, last_name, username, password)

print (str(user1))
