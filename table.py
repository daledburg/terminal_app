# Functions module
import time
from prettytable import PrettyTable
import clearing

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