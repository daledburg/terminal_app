# Functions module
import pickle
import os
import time
from datetime import date
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import clearing
import budget

# Current Date info
current_date = date.today()
current_date = str(current_date)
current_date_split = current_date.split('-')

current_date_split = [int(i) for i in current_date_split]
current_date_split = current_date_split[0:2]
# for i in current_date_split[:]:
#     current_date_split = int(current_date_split[i])

# Menu configuration can be configured for the different menus
def menu(menu_item, menu_item1, menu_item2, menu_item3, menu_item4):
    options = [menu_item, menu_item1, menu_item2, menu_item3, menu_item4]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f'You have seleceted {options[menu_entry_index]}!')
    return options[menu_entry_index]

# function to be used for float inputs
def input_functions(input_type_str, err_type_str):
    while True:
        try:
            return_var = float(input(input_type_str))
            if return_var > 0:
                return return_var
        except ValueError:
            pass
        print(err_type_str)

# Finding weekly values of entry for incomes expense etc.
def pay_timetable(type_str, inc_value, err_str):
    while True:
        try:
            pay_time = input(type_str)
            if pay_time == 'm':
                inc_value = round((inc_value / 4), 2)
                return inc_value
            elif pay_time == 'f':
                inc_value = round((inc_value / 2), 2)
                return inc_value
            elif pay_time == 'w':
                return inc_value
            elif pay_time == 's':
                inc_value = round((inc_value / 26), 2)
                return inc_value
            elif pay_time == 'a':
                inc_value = round((inc_value / 52), 2)
                return inc_value
        except ValueError:
            pass
        print(err_str)

# Function for adding expenses to new or existing users
def print_exp(foo, next_expense, amount_next_expense):
    foo.set_expense(next_expense, amount_next_expense)
    clearing.clear()
    print('Current expenses include: ')
    for i in range(len(foo.expense_description)):
        print(foo.expense_description[i])

# Function to save expenses to new file
def saving_expenses(username, budget_instance):
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')

    outfile = open(filename, 'wb')
    pickle.dump(budget_instance.expense_description, outfile)
    outfile.close()

    outfile1 = open(filename1, 'wb')
    pickle.dump(budget_instance.expense_amount, outfile1)
    outfile1.close()

# Function to save the income data for each user to a new file
def save_income(username, income_save):
    filename2 = ('income_amount' + str(username) + '.dat')

    outfile2 = open(filename2, 'wb')
    pickle.dump(income_save, outfile2)
    outfile2.close()

# Function to access the saved expense data for a user
def open_expenses(username, budget_instance):
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')

    infile = open(filename, 'rb')
    budget_instance.expense_description = pickle.load(infile)
    infile.close()

    infile1 = open(filename1, 'rb')
    budget_instance.expense_amount = pickle.load(infile1)
    infile1.close()

# Function to access the saved income data for each user
def open_income(username):
    filename2 = ('income_amount' + str(username) + '.dat')

    infile2 = open(filename2, 'rb')
    income_save = pickle.load(infile2)
    infile2.close()

    return income_save

# Function to generate and save expenses
def expen_funct(b_instance):
    while True:
        try:
            more_exp = input('Do you want to add an expense? (y/n): ').lower()
            if more_exp == 'y':
                next_expense = input('Provide a description of this expense: ')
                amount_next_expense = input_functions('How much is this expense? $', 'Amount entered must be greater than 0')
                amount_next_expense = pay_timetable('Do you pay this expense weekly, fortnightly, monthly, semi-annually or annually? (w/f/m/s/y) ', amount_next_expense, 'Please enter w, f, m, s or a')
                print_exp(b_instance, next_expense, amount_next_expense)
            elif more_exp == 'n':
                break
        except ValueError:
            pass
        print('Please enter y or n')

# Table of income, expenses and left over money
def display_table(x):
    while True:
        try:
            table_print = input('Would you like to see a breakdown of your entered informtaion? (y/n) ')
            clearing.clear()
            if table_print == 'y':
                expense_table = PrettyTable()
                expense_table.field_names = ['Expense Description', 'Expense Amount per week ($)']
                expense_table.add_row(['Income per week', x.income])

                for i in range(len(x.expense_description)):
                    expense_table.add_row([x.expense_description[i], -(x.expense_amount[i])])

                expense_table.add_row(['Money Left', (x.income - sum(x.expense_amount))])
                expense_table.align['Expense Amount'] = 'r'
                expense_table.align['Expense Description'] = 'r'

                print('This is a breakdown of your current expenses.')
                print(expense_table.get_string(title='Income/Expense Breakdown Table'))
                time.sleep(2)
                break
            elif table_print == 'n':
                print('Okay, lets continue then.')
                break
        except ValueError:
            pass
        print('Please enter y or n')

# Savings Calculator feature function
def savings_calculator(goal_amount, month_int, year_int):
    months_to_pay = (((year_int - current_date_split[0]) * 12) + (month_int - current_date_split[1]))
    contribution_needed = round(((goal_amount / months_to_pay) / 4), 2)
    print(f'You will need to hide away ${contribution_needed} each week to reach your goal!')
    return contribution_needed

# Feature of debt calculator function
def debt_calculator(debt_amount, month_int, year_int, contribution):
    months_to_pay = ((year_int - current_date_split[0]) * 12) + (month_int - current_date_split[1])
    contribution_needed = round((debt_amount / (months_to_pay * 4)), 2)
    contribution_diff = round((contribution_needed - contribution), 2)
    print(f'You currently contribute ${contribution} each week.')
    print(f'To meet your goal you need to contribute ${contribution_needed} per week')
    print(f'That is a difference of ${contribution_diff}')
    return contribution_diff

# Function to get future date for calculators
def future_date(inp_str):
    while True:
        try:
            paid_date = input(f'When do you want to {inp_str} by? format: mm/yyyy ')
            paid_date_ints = paid_date.split('/')

            if len(paid_date_ints) == 2:
                paid_date_ints = [int(i) for i in paid_date_ints]
                if paid_date_ints[0] > 0 and paid_date_ints[0] <= 12:
                    if paid_date_ints[1] > 2021 and paid_date_ints[1] <= 2099:    
                        if paid_date_ints[1] > current_date_split[0]:
                            return paid_date_ints
                        elif paid_date_ints[1] == current_date_split[0]:
                            if paid_date_ints[0] > current_date_split[1]:
                                return paid_date_ints
        except ValueError:
            pass
        print('Enter future date in correct format: mm/yyyy ')

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
        print(f' Users remaining: {list_users}')
        with open('logins_filename.dat', 'wb') as wfp:
            pickle.dump(logins_diction, wfp)

        with open('logins_filename.dat', 'rb') as rfp:
            logins_diction = pickle.load(rfp)

        os.remove(filename)
        os.remove(filename1)
        os.remove(filename2)

        print('User deleted successfully, now exiting.')
        quit()
    elif user_delete == 'n':
        print('Profile not deleted, now exiting.')
        quit()


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

    elif user_delete == 'n':
        print('Profiles not deleted, now exiting.')
        quit()
