# Budgeting app
# Imported packages for application
import sys
import clearing
import pyfiglet
import pyfiglet.fonts
import budget
import functions
import budget_functions
import login_function
import calculators
from table import display_table

 # Strings to be used for input fields
inc_str = "What is your income after tax? $"
not_positive_err = 'Amount entered must be greater than 0'
inc_err_str = 'Please enter w, f, or m'
pay_inc_str = 'How frequently are you paid? (w/f/m): '

if __name__ == '__main__':
    # Menu for budget start
    clearing.clear()
    print(pyfiglet.figlet_format('Budget Buddy!'))
    print('Welcome to budget buddy! Your best buddy for helping you save money!')

    # Handle error if no users created yet
    while True:
        try:
            if_new = functions.menu('Register', 'Existing User','Quit', menu_item3 = None, menu_item4 = None)
            if if_new == 'Register':
                username = login_function.new_user()
                print(f'Hello there {username}, lets get down to saving you money!')

                your_income = functions.input_functions(inc_str, not_positive_err)
                your_income = budget_functions.pay_timetable(pay_inc_str, your_income, inc_err_str)
                budget_functions.save_income(username, your_income)

                clearing.clear()
                p1 = budget.Budget(username, your_income)
                budget_functions.expen_funct(p1)

                clearing.clear()
                spare = p1.spare_cash()
                budget_functions.saving_expenses(username, p1)
                break

    # Use previously saved data to calculate data
            elif if_new == 'Existing User':
                if login_function.any_current_users() is True:
                    username = login_function.current_user()
                    print(f'Hello there {username}, lets get down to saving you money!')
                    # Finding the income of user
                    while True:
                        try:
                            saved_income = input('Would you like to use your saved income? (y/n): ')
                            if saved_income == 'y':
                                your_income = budget_functions.open_income(username)
                                break
                            elif saved_income == 'n':
                                your_income = functions.input_functions(inc_str, not_positive_err)
                                your_income = budget_functions.pay_timetable(pay_inc_str, your_income, inc_err_str)
                                # Create new Saved income file
                                budget_functions.save_income(username, your_income)
                                break
                        except ValueError:
                            pass
                        print('Please enter y or n')
                    p1 = budget.Budget(username, your_income)

                    # Finding the users expenses
                    while True:
                        try:
                            saved_expenses = input('Would you like to use your saved expenses? (y/n): ')
                            if saved_expenses == 'y':
                                budget_functions.open_expenses(username, p1)
                                break
                            elif saved_expenses == 'n':
                                clearing.clear()
                                budget_functions.expen_funct(p1)
                                break
                        except ValueError:
                            pass
                        print('Please enter y or n')
                    clearing.clear()
                    spare = p1.spare_cash()
                    budget_functions.saving_expenses(username, p1)
                    break
            # let user quit
            elif if_new == 'Quit':
                print('Goodbye!')
                sys.exit()
        except Exception:
            pass
        print('No current users, please register')

    # Display Table to show user breakdown of expenses against income and leftover money
    display_table(p1)
    # What feature would they like to do next?
    print('There are more features to explore.')
    # Loop to let user use each of the features as they want
    while True:
        next_feature = functions.menu('Savings Calculator', 'Debt Relief Calculator', 'Delete User Profile', 'Delete All Users Profiles', 'Quit')
        clearing.clear()
        # Savings calculator feature
        if next_feature == 'Savings Calculator':
            clearing.clear()
            savings_goal = functions.input_functions('What is your savings goal? $', not_positive_err)
            time_goal = calculators.future_date('save this')
            calculators.savings_calculator(savings_goal, time_goal[0], time_goal[1])
        # Debt Relief Feature
        elif next_feature == 'Debt Relief Calculator':
            clearing.clear()
            balance_owed = functions.input_functions('What is the balance owed on the outstanding debt? $', not_positive_err)
            while True:
                try:
                    current_contribution = float(input('What is your current regualar contribution to this debt? $'))
                    if current_contribution > 0.0 and current_contribution < balance_owed:
                        break
                except ValueError:
                    pass
                print('Your current contribution must be a positve number and less than balance owed.')
            cont_time = budget_functions.pay_timetable('How often do you contribute money towards paying this debt off? (w/f/m) ', current_contribution, inc_err_str)
            time_goal = calculators.future_date('have this paid off')
            calculators.debt_calculator(balance_owed, time_goal[0], time_goal[1], current_contribution)
        # Delete current user and any saved data
        elif next_feature == 'Delete User Profile':
            clearing.clear()
            login_function.delete_user(username)
            sys.exit()
        # Delete all current users, cleans up system, need master password
        elif next_feature == 'Delete All Users Profiles':
            clearing.clear()
            login_function.delete_all_users()
            sys.exit()
        # let user quit
        elif next_feature == 'Quit':
            clearing.clear()
            print(f'Thank you {username} using this application, have a nice day!')
            sys.exit()
