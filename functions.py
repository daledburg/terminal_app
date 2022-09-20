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


def wrong_user_menu():
    options1 = ['Try Again?', 'Quit']
    terminal_menu1 = TerminalMenu(options1)
    menu_entry_index1 = terminal_menu1.show()
    return options1[menu_entry_index1]

def pay_timetable():
#     your_income = 0
    your_income = float(input("What is your income after tax? "))
    pay_time = input("Are you paid weekly, fortnightly, or monthly? (w/f/m) ")
    if pay_time == 'm':
        your_income = your_income / 4
        return your_income
    elif pay_time == 'f':
        your_income = your_income / 2
        return your_income
    elif pay_time == 'w':
        return your_income

def display_table(x):
    expense_table = PrettyTable()

    expense_table.field_names = ['Expense Description', 'Expense Amount ($)']

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
