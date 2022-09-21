# Login functionality
import pickle
import os
import functions
import clearing

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
            clearing.clear()
            if len(username) > 0 and len(username) < 20:
                password = input('Input a password that is 6-16 characters long: ')
                clearing.clear()
                try:
                    if len(password) >= 6 and len(password) <= 16:
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
        cont_or_quit = functions.wrong_user_menu()
        if cont_or_quit == 'Quit':
            quit()
        elif cont_or_quit == 'Try Again?':
            clearing.clear()
            continue

    return inp_user
