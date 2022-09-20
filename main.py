# Budgeting app
# Imported packages for application
import pickle
import os
import clearing
import time
import budget
import functions
import login_function

# Menu for budget start
clearing.clear()
print('Welcome to budget buddy! Your best buddy for helping you save money!')
if_new = functions.menu()

# Complete new budget
if if_new == 'Register':
    username = login_function.new_user()

    your_name = username
    print(f'Hello there {your_name}, lets get down to saving you money!')

    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')
    filename2 = ('income_amount' + str(username) + '.dat')

    your_income = functions.pay_timetable()

    clearing.clear()

    p1 = budget.Budget(your_name, your_income)

    functions.adding_expenses(p1)

    clearing.clear()

    spare = p1.spare_cash()

    outfile = open(filename, 'wb')
    pickle.dump(p1.expense_description, outfile)
    outfile.close()

    outfile1 = open(filename1, 'wb')
    pickle.dump(p1.expense_amount, outfile1)
    outfile1.close()

    outfile2 = open(filename2, 'wb')
    pickle.dump(your_income, outfile2)
    outfile2.close()
# Use previously saved data to calculate data
elif if_new == 'Existing User':
    username = login_function.current_user()
    your_name = username
    # Create filenames to save data for later use
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')
    filename2 = ('income_amount' + str(username) + '.dat')
    
    print(f'Hello there {your_name}, lets get down to saving you money!')
    # Finding the income of user
    saved_income = input('Would you like to use your saved income? (y/n): ')
    if saved_income == 'n':
        your_income = functions.pay_timetable()
        # Create new Saved income file
        outfile2 = open(filename2, 'wb')
        pickle.dump(your_income, outfile2)
        outfile2.close()
    elif saved_income == 'y':
        infile2 = open(filename2, 'rb')
        your_income = pickle.load(infile2)
        infile2.close()

    p1 = budget.Budget(your_name, your_income)
    # Finding the users expenses 
    saved_expenses = input('Would you like to use your saved expenses? (y/n): ')
    if saved_expenses == 'y':
        infile = open(filename, 'rb')
        p1.expense_description = pickle.load(infile)
        infile.close()

        infile1 = open(filename1, 'rb')
        p1.expense_amount = pickle.load(infile1)
        infile1.close()
    elif saved_expenses == 'n':
        functions.adding_expenses(p1)

    clearing.clear()

    spare = p1.spare_cash()
# let user quit
elif if_new == 'Quit':
    print('Goodbye!')
    quit()

# Display Table to show user breakdown of expenses against income and leftover money
functions.display_table(p1)

time.sleep(3)

# What feature would they like to do next?
print('There are more features to explore.')
# Loop to let user use each of the features as they want
while True:
    next_feature = functions.further_features()
    clearing.clear()
    if next_feature == 'Savings Calculator':
        clearing.clear()
        functions.savings_calculator()
    elif next_feature == 'Debt Relief Calculator':
        functions.debt_calculator()
    # Delete current user and any saved data
    elif next_feature == 'Delete User Profile':
        delete_user = input('Are you sure you want to delete this user? (y/n): ')
        if delete_user == 'y':
            with open('logins_filename.dat', 'rb') as rfp:
                logins_diction = pickle.load(rfp)
                logins_diction.pop(username)
            print(logins_diction)
            with open('logins_filename.dat', 'wb') as wfp:
                pickle.dump(logins_diction, wfp)

            with open('logins_filename.dat', 'rb') as rfp:
                logins_diction = pickle.load(rfp)
            # logins_diction.pop(username)
            os.remove(filename)
            os.remove(filename1)
            os.remove(filename2)

            print('User deleted successfully, now exiting.')
            quit()
    # let user quit
    elif next_feature == 'Quit':
        clearing.clear()
        print('Thank you for using this application, have a nice day!')
        quit()
