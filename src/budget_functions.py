# Functions module for budget inputs
import pickle
import clearing
from functions import input_functions

# Finding weekly values of entry for incomes expense etc.
def pay_timetable(type_str, inc_value, err_str):
    while True:
        try:
            pay_time = input(type_str).lower()
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
                amount_next_expense = pay_timetable('Do you pay this expense weekly, fortnightly, monthly, semi-annually or annually? (w/f/m/s/a) ', amount_next_expense, 'Please enter w, f, m, s or a')
                print_exp(b_instance, next_expense, amount_next_expense)
            elif more_exp == 'n':
                break
        except ValueError:
            pass
        print('Please enter y or n')