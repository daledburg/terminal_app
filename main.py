# Budgeting app

# Imported packages for application
from prettytable import PrettyTable
from simple_term_menu import TerminalMenu
import pickle
import budget
import functions


# Set files to export data for later use
filename = 'exp_desc'
filename1 = 'exp_amount'
existing_logins = 'ex_logins'
logins_dict = {}

if_new = functions.menu()

# your_name = input('Hello, What is your name? ')

# Complete new budget
if if_new == 'Register':
    your_name = input('Hello, What is your name? ')

    print(f'Hello there {your_name.capitalize()}, lets get down to saving you money!')

    your_income = functions.pay_timetable()

    p1 = budget.Budget(your_name, your_income)

    while True:
        more_exp = input('Do you want to add an expense? (y/n): ')
        if more_exp == 'y':
            p1.set_expense((input('What is this expense? ')), (float(input('How much is this expense? '))))
        elif more_exp == 'n':
            break

    p1.spare_cash()

    outfile = open(filename, 'wb')
    pickle.dump(p1.expense_description, outfile)
    outfile.close()

    outfile1 = open(filename1, 'wb')
    pickle.dump(p1.expense_amount, outfile1)
    outfile1.close()
# Use previously saved data to calculate data
elif if_new == 'Existing User':
    print(f'Hello there {your_name.capitalize()}, lets get down to saving you money!')

    your_income = functions.pay_timetable()
    p1 = budget.Budget(your_name, your_income)
    
    infile = open(filename, 'rb')
    p1.expense_description = pickle.load(infile)
    infile.close()

    infile1 = open(filename1, 'rb')
    p1.expense_amount = pickle.load(infile1)
    infile1.close()

    p1.spare_cash()

# Display Table to show user breakdown of expenses against income and leftover money
expense_table = PrettyTable()

expense_table.field_names = ['Expense Description', 'Expense Amount ($)']

expense_table.add_row(['Income per week', p1.income])

for i in range(len(p1.expense_description)):
    expense_table.add_row([p1.expense_description[i], -(p1.expense_amount[i])])

expense_table.add_row(['Money Left', (p1.income - sum(p1.expense_amount))])

expense_table.align['Expense Amount'] = 'r'
expense_table.align['Expense Description'] = 'r'
# print(expense_table.get_string(title='Income/Expense Breakdown Table'))

table_print = input(f'So {your_name} would you like to see a breakdown of your entered informtaion? (y/n) ')

# Ask user if they would like to display this table
if table_print == 'y':
    print('This is a breakdown of your current expenses.')
    print(expense_table.get_string(title='Income/Expense Breakdown Table'))
elif table_print == 'n':
    print('Okay, lets continue then.')

# What feature would they like to do next?
print('There are more features to explore.')
feature_select = input('What feature would you like to move onto')
# Savings goal breakdown
gg = float(input('How much is your current savings goal? '))
tt = float(input('How many months do you have to save? '))

s1 = budget.SavingGoal(p1, p1, gg, tt)

s1.find_required_amount()

# Debt relief calcualtor
