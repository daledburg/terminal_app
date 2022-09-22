# Functions module
from simple_term_menu import TerminalMenu

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

