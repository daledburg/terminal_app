# Budgeting app

# Imported packages for application
from prettytable import PrettyTable
from simple_term_menu import TerminalMenu
import pickle
import os
import budget
import functions
import login_function
import clearing

# Menu for budget start
clearing.clear()
print('Welcome to budget buddy! Your one stop application for helping you to save money!')
if_new = functions.menu()

# Complete new budget
if if_new == 'Register':
    username = login_function.new_user()

    your_name = username
    print(f'Hello there {your_name}, lets get down to saving you money!')

    filename = ('exp_desc' + str(username))
    filename1 = ('exp_amount' + str(username))

    your_income = functions.pay_timetable()

    clearing.clear()

    p1 = budget.Budget(your_name, your_income)

    while True:
        more_exp = input('Do you want to add an expense? (y/n): ')
        if more_exp == 'y':
            p1.set_expense((input('What is this expense? ')), (float(input('How much is this expense? '))))
        elif more_exp == 'n':
            break

    clearing.clear()

    p1.spare_cash()

    outfile = open(filename, 'wb')
    pickle.dump(p1.expense_description, outfile)
    outfile.close()

    outfile1 = open(filename1, 'wb')
    pickle.dump(p1.expense_amount, outfile1)
    outfile1.close()
# Use previously saved data to calculate data
elif if_new == 'Existing User':
    username = login_function.current_user()
    your_name = username
    # print(f'Hello there {your_name}, lets get down to saving you money!')
    
    filename = ('exp_desc' + str(username))
    filename1 = ('exp_amount' + str(username))
    
    print(f'Hello there {your_name}, lets get down to saving you money!')

    your_income = functions.pay_timetable()
    p1 = budget.Budget(your_name, your_income)
    
    infile = open(filename, 'rb')
    p1.expense_description = pickle.load(infile)
    infile.close()

    infile1 = open(filename1, 'rb')
    p1.expense_amount = pickle.load(infile1)
    infile1.close()

    p1.spare_cash()
elif if_new == 'Quit':
    print('Goodbye!')
    quit()

# Display Table to show user breakdown of expenses against income and leftover money
functions.display_table(p1)

# What feature would they like to do next?
print('There are more features to explore.')
# Savings goal breakdown
while True:
    next_feature = functions.further_features()
    clearing.clear()
    if next_feature == 'Savings Calculator':
        clearing.clear()
        gg = float(input('How much is your current savings goal? $'))
        clearing.clear()
        tt = float(input('How many months do you have to save? '))
        clearing.clear()
        s1 = budget.SavingGoal(p1, p1, gg, tt)

        s1.find_required_amount()
        # Debt relief calcualtor
    elif next_feature == 'Debt Relief Calculator':
        print('debt relief')
    elif next_feature == 'Quit':
        clearing.clear()
        print('Thank you for using this application, have a nice day!')
        quit()    

