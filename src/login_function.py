# Login functionality
import sys
import pickle
import os
import clearing
from functions import menu

# New user function
def new_user():
    logins_filename = 'logins_filename.dat'
    logins_diction = {}
    if os.path.exists(logins_filename):
        with open(logins_filename, 'rb') as rfp:
            logins_diction = pickle.load(rfp)

    while True:
        try:
            username = str(input('What would you like your Username to be? '))
            if len(username) > 0 and len(username) < 20:
                password = input('Input a password that is 6-16 characters long: ')
                try:
                    if len(password) >= 6 and len(password) <= 16:
                        clearing.clear()
                        break
                except ValueError:
                    pass
                
                if len(password) > 16:
                    print('Password too long, must be between 6 and 16 characters long, try again: ')
        except ValueError:
            pass
        if len(username) is 0 or len(password) > 20:
            print('Username must be between 1-20 characters long, try again: ')
        elif len(password) <= 6 or len(password) > 16:
            print('Password must be between 6 and 16 characters long, try again: ')

    # logins = username, password
    logins_diction[username] = password

    with open(logins_filename, 'wb') as wfp:
        pickle.dump(logins_diction, wfp)

    with open(logins_filename, 'rb') as rfp:
        logins_diction = pickle.load(rfp)

    return username
# Function to check if any current users
def any_current_users():
    logins_filename = 'logins_filename.dat'
    logins_diction = {}
    with open(logins_filename, 'rb') as rfp:
        logins_diction = pickle.load(rfp)

    current_keys = list(dict.keys(logins_diction))
    if len(current_keys) == 0:
        return False
    else:
        print('Current Users: ')
        for i in range(len(current_keys)):
            print(current_keys[i])
        return True

# Recall current users login
def current_user():
    logins_filename = 'logins_filename.dat'
    logins_diction = {}
    with open(logins_filename, 'rb') as rfp:
        logins_diction = pickle.load(rfp)

    while True:
        try:
            inp_user = input('Username: ')
            inp_pwd = input('Password: ')
            if inp_user in logins_diction and logins_diction[inp_user] == inp_pwd:
                clearing.clear()
                print('Login success!')
                break
        except Exception:
            pass
        cont_or_quit = menu('Try Again?', 'Quit', menu_item2 = None, menu_item3  = None, menu_item4  = None)
        if cont_or_quit == 'Quit':
            sys.exit()
        elif cont_or_quit == 'Try Again?':
            clearing.clear()
            continue

    return inp_user

# Function to delete single user that is logged in
def delete_user(username):
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')
    filename2 = ('income_amount' + str(username) + '.dat')
    user_delete = input('Are you sure you want to delete this user? (y/n): ')
    if user_delete == 'y':
        with open('logins_filename.dat', 'rb') as rfp:
            logins_diction = pickle.load(rfp)
            logins_diction.pop(username)
        list_users = list(dict.keys(logins_diction))
        print(f' Users remaining: {list_users}')\

        with open('logins_filename.dat', 'wb') as wfp:
            pickle.dump(logins_diction, wfp)

        with open('logins_filename.dat', 'rb') as rfp:
            logins_diction = pickle.load(rfp)

        os.remove(filename)
        os.remove(filename1)
        os.remove(filename2)
        print('User deleted successfully, now exiting.')
        sys.exit()
    elif user_delete == 'n':
        print('Profile not deleted, now exiting.')
        sys.exit()

# Function to delete all users data from the database
def delete_all_users():
    user_delete = input('Are you sure you want to delete all users? (y/n): ')
    if user_delete == 'y':
        sure_question = input('Please enter master password to delete all users: ')
        if sure_question == 'DeletePassword':
            test = os.listdir('.')
            for item in test:
                if item.endswith('.dat'):
                    os.remove(item)
                    print('Profiles deleted successfully')
    elif user_delete == 'n':
        print('Profiles not deleted, now exiting.')
