# Budgeting app
from prettytable import PrettyTable
import pickle
import budget

# Welcome and ask name
your_income = 0

def pay_timetable():
    pay_time = input("Are you paid weekly, fortnightly, or monthly? (w/f/m) ")
    if pay_time == 'm':
        your_income = your_income / 4
    elif pay_time == 'f':
        your_income = your_income / 2
    elif pay_time == 'w':
        return your_income


filename = 'exp_desc'
filename1 = 'exp_amount'
your_name = input('Hello, What is your name? ')
been_here_before = input("Welcome to your personal budgeting buddy. Have you been here before? (y/n) ")
# print(f'Hello there {your_name.capitalize()}, lets get down to saving you money!')


if been_here_before == 'n':

    print(f'Hello there {your_name.capitalize()}, lets get down to saving you money!')
    your_income = float(input("What is your income after tax? "))
    pay_timetable()

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

elif been_here_before == 'y':
    print(f'Hello there {your_name.capitalize()}, lets get down to saving you money!')
    your_income = float(input("What is your income after tax? "))
    pay_timetable()
    p1 = budget.Budget(your_name, your_income)
    
    infile = open(filename, 'rb')
    p1.expense_description = pickle.load(infile)
    infile.close()

    infile1 = open(filename1, 'rb')
    p1.expense_amount = pickle.load(infile1)
    infile1.close()

    p1.spare_cash()

expense_table = PrettyTable()

expense_table.field_names = ['Expense Description', 'Expense Amount ($)']

expense_table.add_row(['Income', p1.income])

for i in  range(len(p1.expense_description)):
    expense_table.add_row([p1.expense_description[i], -(p1.expense_amount[i])])

expense_table.add_row(['Money Left', (p1.income - sum(p1.expense_amount))])

expense_table.align['Expense Amount'] = 'r'
expense_table.align['Expense Description'] = 'r'
# print(expense_table.get_string(title='Income/Expense Breakdown Table'))

table_print = input(f'So {your_name} would you like to see a breakdown of your entered informtaion? (y/n) ')

if table_print == 'y':
    print('This is a breakdown of your current expenses.')
    print(expense_table.get_string(title='Income/Expense Breakdown Table'))
elif table_print == 'n':
    print('Okay, lets continue then.')

gg = float(input('How much is your current savings goal? '))
tt = float(input('How many months do you have to save? '))

s1 = budget.SavingGoal(p1, p1, gg, tt)

s1.find_required_amount()
