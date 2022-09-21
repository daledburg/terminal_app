# Budgeting app
# Imported packages for application
from ast import Try
import time
import clearing
import budget
import functions
import login_function

# Menu for budget start
clearing.clear()
print('Welcome to budget buddy! Your best buddy for helping you save money!')

exp_str = 'Do you want to add an expense? (y/n): '
not_positive_err = 'Amount entered must be greater than 0'
inc_err_str = 'Please enter w, f, or m'
exp_ttable = 'Do you pay this expense weekly, fortnightly, monthly, semi-annually or annually? (w/f/m/s/y) '
 
# Handle error if no users created yet
while True:
    try:
        if_new = functions.menu()
        if if_new == 'Register':
            username = login_function.new_user()
            print(f'Hello there {username}, lets get down to saving you money!')

            while True:
                try:
                    your_income = float(input("What is your income after tax? $"))
                    if your_income > 0.0:
                        break
                except ValueError:
                    pass
                print('Your income must be a positve number')

            your_income = functions.pay_timetable(your_income)

            functions.save_income(username, your_income)
            clearing.clear()
            p1 = budget.Budget(username, your_income)
            while True:
                try:
                    more_exp = input('Do you want to add an expense? (y/n): ')
                    if more_exp == 'y':
                        amount_next_expense = functions.input_functions(exp_str, not_positive_err)
                        amount_next_expense = functions.pay_timetable(exp_ttable, amount_next_expense, 'Please enter w, f, m, s or a')            functions.adding_expenses(p1)
                        
            clearing.clear()
            spare = p1.spare_cash()
            functions.saving_expenses(username, p1)
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
                        pay_inc_str = 'How frequently are you paid? (w/f/m): '
                        
                        if saved_income == 'y':
                            your_income = functions.open_income(username)
                            break
                        elif saved_income == 'n':
                            while True:
                                try:
                                    your_income = float(input("What is your income after tax? $"))
                                    if your_income > 0.0:
                                        break
                                except ValueError:
                                    pass
                                print('Your income must be a positve number')

                            your_income = functions.pay_timetable(pay_inc_str, your_income, inc_err_str)
                            # Create new Saved income file
                            functions.save_income(username, your_income)
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
                            functions.open_expenses(username, p1)
                            break
                        elif saved_expenses == 'n':

                            functions.adding_expenses(p1)
                            break
                    except ValueError:
                        pass
                    print('Please enter y or n')
                clearing.clear()
                spare = p1.spare_cash()
                break
        # let user quit
        elif if_new == 'Quit':
            print('Goodbye!')
            quit()
    except Exception:
        pass
    print('No current users, please register')

# Display Table to show user breakdown of expenses against income and leftover money
functions.display_table(p1)

# What feature would they like to do next?
print('There are more features to explore.')

# Loop to let user use each of the features as they want
while True:
    next_feature = functions.further_features()

    clearing.clear()

    if next_feature == 'Savings Calculator':
        clearing.clear()
        save_str = 'save this'
        while True:
            try:
                savings_goal = float(input('What is your savings goal? $'))
                if savings_goal > 0.0:
                    break
            except ValueError:
                pass
            print('Your goal must be a positve number')

        time_goal = functions.future_date(save_str)

        functions.savings_calculator(savings_goal, time_goal[0], time_goal[1])

    elif next_feature == 'Debt Relief Calculator':
        clearing.clear()

        debt_str = 'have this paid off'
        cont_str = 'How often do contribute? (w/f/m) '

        while True:
            try:
                balance_owed = float(input('What is the balance owed on the outstanding debt? $'))
                if balance_owed > 0.0:
                    break
            except ValueError:
                pass
            print('Your balance must be a positve number')

        while True:
            try:
                current_contribution = float(input('What is your current regualar contribution to this debt? $'))
                if current_contribution > 0.0 and current_contribution < balance_owed:
                    break
            except ValueError:
                pass
            print('Your current contribution must be a positve number and less than balance owed.')
        cont_time = functions.pay_timetable(cont_str, current_contribution)
        time_goal = functions.future_date(debt_str, time_goal[0], time_goal[1], cont_time)
        functions.debt_calculator()

    # Delete current user and any saved data
    elif next_feature == 'Delete User Profile':
        clearing.clear()
        functions.delete_user(username)
        
    # let user quit
    elif next_feature == 'Quit':
        clearing.clear()
        print(f'Thank you {username} using this application, have a nice day!')
        quit()
