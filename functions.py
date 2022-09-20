from simple_term_menu import TerminalMenu

# Menu configuration
def menu():
    options = ['Register', 'Existing User', 'Option 3']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f'You have seleceted {options[menu_entry_index]}!')


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
