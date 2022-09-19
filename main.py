# Budgeting app
from prettytable import PrettyTable
from budget import Budget

# Welcome and ask name
your_name = input("Welcome to your personal budgeting buddy. What is your name? ")

print(f'Well hello there {your_name.capitalize()}, lets get down to saving you money!')

your_income = float(input("What is your income after tax? "))

pay_timetable = input("Are you paid weekly, fortnightly, or monthly? (w/f/m) ")

if pay_timetable == 'm':
    your_income = your_income / 4
elif pay_timetable == 'f':
    your_income = your_income / 2

p1 = Budget(your_name, your_income)

while True:
    more_exp = input('Do you want to add an expense? (y/n): ')
    if more_exp == 'y':
        p1.set_expense((input('What is this expense? ')), (float(input('How much is this expense? '))))
    elif more_exp == 'n':
        break

p1.spare_cash()

my_table = PrettyTable()

my_table.field_names = ['Expense Description', 'Expense Amount']

# my_table.add_row(('Income'), p1.income)

for i in  range(len(p1.expense_description)):
    my_table.add_row([p1.expense_description[i], -(p1.expense_amount[i])])

table_print = input(f'So {your_name} would you like to see a breakdown of your entered informtaion? (y/n) ')

if table_print == 'y':
    print('This is a breakdown of your current expenses.')
    print(my_table)
elif table_print == 'n':
    print('Okay, lets continue then.')
