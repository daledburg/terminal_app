import pickle
import os
from datetime import date
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import clearing

# Menu configuration
def menu():
    options = ['Register', 'Existing User', 'Quit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f'You have seleceted {options[menu_entry_index]}!')
    return options[menu_entry_index]

# Menu if you entered wrong information
def wrong_user_menu():
    options1 = ['Try Again?', 'Quit']
    terminal_menu1 = TerminalMenu(options1)
    menu_entry_index1 = terminal_menu1.show()
    return options1[menu_entry_index1]

# Menu to select other features
def further_features():
    options2 = ['Savings Calculator', 'Debt Relief Calculator', 'Delete User Profile', 'Quit']
    terminal_menu2 = TerminalMenu(options2)
    menu_entry_index2 = terminal_menu2.show()
    return options2[menu_entry_index2]

# Calculates income per week
def pay_timetable():
    while True:
        try:
            your_income = float(input("What is your income after tax? $"))
            if your_income > 0.0:
                break
        except ValueError:
            pass
        print('Your income must be a positve number')

    while True:
        try:
            pay_time = input("Are you paid weekly, fortnightly, or monthly? (w/f/m) ")
            if pay_time == 'm':
                your_income = your_income / 4
                return your_income
            elif pay_time == 'f':
                your_income = your_income / 2
                return your_income
            elif pay_time == 'w':
                return your_income
        except ValueError:
            pass
        print('Please enter either w, f or m')
        
# Table of income, expenses and left over money
def display_table(x):
    expense_table = PrettyTable()

    expense_table.field_names = ['Expense Description', 'Expense Amount per week ($)']

    expense_table.add_row(['Income per week', x.income])

    for i in range(len(x.expense_description)):
        expense_table.add_row([x.expense_description[i], -(x.expense_amount[i])])

    expense_table.add_row(['Money Left', (x.income - sum(x.expense_amount))])

    expense_table.align['Expense Amount'] = 'r'
    expense_table.align['Expense Description'] = 'r'
    # print(expense_table.get_string(title='Income/Expense Breakdown Table'))

    table_print = input('Would you like to see a breakdown of your entered informtaion? (y/n) ')
    clearing.clear()
    if table_print == 'y':
        print('This is a breakdown of your current expenses.')
        print(expense_table.get_string(title='Income/Expense Breakdown Table'))
    elif table_print == 'n':
        print('Okay, lets continue then.')

# Feature of debt calculator function
def debt_calculator():
    while True:
        try:
            balance_owed = float(input('What is the balance owed on the outstanding debt? $'))
            if balance_owed > 0.0:
                break
        except ValueError:
            pass
        print('Your balance must be a positve number')

    while True:
        try:
            current_contribution = float(input('What is your current regualar contribution to this debt? $'))
            if current_contribution > 0.0 and current_contribution < balance_owed:
                break
        except ValueError:
            pass
        print('Your current contribution must be a positve number and less than balance owed.')

    while True:
        try:
            frequency_of_contribution = (input('Do you pay this expense weekly, fortnightly, monthly? (w/f/m) ')).lower()
            if frequency_of_contribution == 'f':
                current_contribution = round((current_contribution / 2), 2)
                break
            elif frequency_of_contribution == 'm':
                current_contribution = round((current_contribution / 4), 2)
                break
            elif frequency_of_contribution == 'w':
                break
        except ValueError:
            pass
        print('Please enter either w, f or m')

    current_date = date.today()

    current_date = str(current_date)

    current_date_split = current_date.split('-')

    current_year_int = int(current_date_split[0])
    current_month_int = int(current_date_split[1])

    while True:
        try:
            paid_date = input('When do you want to pay this off by? format: mm/yyyy '))
            paid_date_ints = paid_date.split('/')
            if len(paid_date_ints) == 2:
                month_int = int(paid_date_ints[0])
                year_int = int(paid_date_ints[1])
                if month_int > 0 and month_int <= 12:
                    if year_int > 2021 and year_int <= 2099:    
                        if year_int > current_year_int:
                            break
                        elif year_int == current_year_int:
                            if month_int > current_month_int:
                                break
        except ValueError:
            pass
        print('Enter future date in correct format: mm/yyyy ')

    months_to_pay = ((year_int - current_year_int) * 12) + (month_int - current_month_int)

    contribution_needed = round(((balance_owed / months_to_pay) / 4), 2)

    contribution_diff = round((contribution_needed - current_contribution), 2)

    print(f'You currently contribute ${current_contribution} each week.')
    print(f'To meet your goal you need to contribute ${contribution_needed} per week')
    print(f'That is a difference of ${contribution_diff}')

# Function for adding expenses to new or existing users
def adding_expenses(foo):
    while True:
        try:
            more_exp = input('Do you want to add an expense? (y/n): ')
            if more_exp == 'y':
                next_expense = input('What is this expense? ')
                amount_next_expense = float(input('How much is this expense? $'))
                frequency_of_expense = (input('Do you pay this expense weekly, fortnightly, monthly, semi-annually or annually? (w/f/m/s/y) ')).lower()
                if frequency_of_expense == 'f':
                    amount_next_expense = round((amount_next_expense / 2), 2)
                elif frequency_of_expense == 'm':
                    amount_next_expense = round((amount_next_expense / 4), 2)
                elif frequency_of_expense == 's':
                    amount_next_expense = round((amount_next_expense / 26), 2)
                elif amount_next_expense == 'y':
                    amount_next_expense = round((amount_next_expense / 52), 2)
                foo.set_expense(next_expense, amount_next_expense)

                clearing.clear()

                print('Current expenses include: ')

                for i in range(len(foo.expense_description)):
                    print(foo.expense_description[i])

            elif more_exp == 'n':
                break
            else:
                print('Please answer y or n.')
        except ValueError:
            pass

def savings_calculator():
    while True:
        try:
            savings_goal = float(input('What is your savings goal? $'))
            if savings_goal > 0.0:
                break
        except ValueError:
            pass
        print('Your goal must be a positve number')

    paid_date1 = input('When do you want to save this by? format: mm/yyyy ')

    current_date1 = date.today()

    current_date1 = str(current_date1)

    current_date_split1 = current_date1.split('-')

    current_year_int1 = int(current_date_split1[0])
    current_month_int1 = int(current_date_split1[1])

    while True:
        try:
            paid_date1 = input('When do you want to save this by? format: mm/yyyy ')
            paid_date_ints1 = paid_date1.split('/')
            if len(paid_date_ints1) == 2:
                month_int1 = int(paid_date_ints1[0])
                year_int1 = int(paid_date_ints1[1])
                if month_int1 > 0 and month_int1 <= 12:
                    if year_int1 > 2021 and year_int1 <= 2099:    
                        if year_int1 > current_year_int1:
                            break
                        elif year_int1 == current_year_int1:
                            if month_int1 > current_month_int1:
                                break
        except ValueError:
            pass
        print('Enter future date in correct format: mm/yyyy ')

    months_to_pay1 = ((year_int1 - current_year_int1) * 12) + (month_int1 - current_month_int1)

    contribution_needed1 = round(((savings_goal / months_to_pay1) / 4), 2)

    print(f'You will need to hide away ${contribution_needed1} each week to reach your goal!')

def saving_expenses(username, budget_instance):
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')

    outfile = open(filename, 'wb')
    pickle.dump(budget_instance.expense_description, outfile)
    outfile.close()

    outfile1 = open(filename1, 'wb')
    pickle.dump(budget_instance.expense_amount, outfile1)
    outfile1.close()

def save_income(username, income_save):
    filename2 = ('income_amount' + str(username) + '.dat')

    outfile2 = open(filename2, 'wb')
    pickle.dump(income_save, outfile2)
    outfile2.close()

def open_expenses(username, budget_instance):
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')

    infile = open(filename, 'rb')
    budget_instance.expense_description = pickle.load(infile)
    infile.close()

    infile1 = open(filename1, 'rb')
    budget_instance.expense_amount = pickle.load(infile1)
    infile1.close()

def open_income(username):
    filename2 = ('income_amount' + str(username) + '.dat')

    infile2 = open(filename2, 'rb')
    income_save = pickle.load(infile2)
    infile2.close()

    return income_save

def delete_user(username):
    filename = ('exp_desc' + str(username) + '.dat')
    filename1 = ('exp_amount' + str(username) + '.dat')
    filename2 = ('income_amount' + str(username) + '.dat')
    user_delete = input('Are you sure you want to delete this user? (y/n): ')
    if user_delete == 'y':
        with open('logins_filename.dat', 'rb') as rfp:
            logins_diction = pickle.load(rfp)
            logins_diction.pop(username)
        print(logins_diction)
        with open('logins_filename.dat', 'wb') as wfp:
            pickle.dump(logins_diction, wfp)

        with open('logins_filename.dat', 'rb') as rfp:
            logins_diction = pickle.load(rfp)
            
        os.remove(filename)
        os.remove(filename1)
        os.remove(filename2)

        print('User deleted successfully, now exiting.')
        quit()

    if user_delete == 'n':
        print('Profile not deleted, now exiting.')
        quit()
