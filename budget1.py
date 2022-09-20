import pickle
import os

logins_filename = 'logins_filename.dat'

logins_diction = {}

if os.path.exists(logins_filename):
    with open(logins_filename, 'rb') as rfp:
        logins_diction = pickle.load(rfp)

username = input('What would you like your Username to be? ')

password = input('What would you like your password to be? ') 

logins = username, password
logins_diction[username] = password

with open(logins_filename, 'wb') as wfp:
    pickle.dump(logins_diction, wfp)

with open(logins_filename, 'rb') as rfp:
    logins_diction = pickle.load(rfp)

print(logins_diction)
