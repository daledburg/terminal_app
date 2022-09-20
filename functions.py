from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import clearing
from datetime import date
from budget import Budget

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
    your_income = float(input("What is your income after tax? $"))
    pay_time = input("Are you paid weekly, fortnightly, or monthly? (w/f/m) ")
    if pay_time == 'm':
        your_income = your_income / 4
        return your_income
    elif pay_time == 'f':
        your_income = your_income / 2
        return your_income
    elif pay_time == 'w':
        return your_income

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
    balance_owed = float(input('What is the balance owed on the outstanding debt? $'))
    current_contribution = float(input('What is the current contribution to this debt? $'))
    
    frequency_of_contribution = (input('Do you pay this expense weekly, fortnightly, monthly? (w/f/m) ')).lower()
    if frequency_of_contribution == 'f':
        current_contribution = round((current_contribution / 2), 2)
    elif frequency_of_contribution == 'm':
        current_contribution = round((current_contribution / 4), 2)


    paid_date = input('When do you want to pay this off by? format: mm/yyyy ')
    paid_date_ints = paid_date.split('/')

    month_int = int(paid_date_ints[0])
    year_int = int(paid_date_ints[1])

    current_date = date.today()

    current_date = str(current_date)

    current_date_split = current_date.split('-')

    current_year_int = int(current_date_split[0])
    current_month_int = int(current_date_split[1])

    months_to_pay = ((year_int - current_year_int) * 12) + (month_int - current_month_int)

    contribution_needed = round(((balance_owed / months_to_pay) / 4), 2)

    contribution_diff = round((contribution_needed - current_contribution), 2)

    print(f'You currently contribute ${current_contribution} each week.')
    print(f'To meet your goal you need to contribute ${contribution_needed} per week')
    print(f'That is a difference of ${contribution_diff}')
# Function for adding expenses to new or existing users
def adding_expenses(foo):
    while True:
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

            print(f'Current expenses include: ')

            for i in range(len(foo.expense_description)):
                print(foo.expense_description[i])

        elif more_exp == 'n':
            break

def savings_calculator():
    savings_goal = float(input('What is your savings goal? $'))

    paid_date1 = input('When do you want to save this by? format: mm/yyyy ')
    paid_date_ints1 = paid_date1.split('/')

    month_int1 = int(paid_date_ints1[0])
    year_int1 = int(paid_date_ints1[1])

    current_date1 = date.today()

    current_date1 = str(current_date1)

    current_date_split1 = current_date1.split('-')

    current_year_int1 = int(current_date_split1[0])
    current_month_int1 = int(current_date_split1[1])

    months_to_pay1 = ((year_int1 - current_year_int1) * 12) + (month_int1 - current_month_int1)

    contribution_needed1 = round(((savings_goal / months_to_pay1) / 4), 2)

    print(f'You will need to hide away ${contribution_needed1} each week to reach your goal!')

