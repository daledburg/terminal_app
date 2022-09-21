# Budgeting app
# Imported packages for application
import pickle
import os
import time
import clearing
import budget
import functions
import login_function

# Menu for budget start
clearing.clear()
print('Welcome to budget buddy! Your best buddy for helping you save money!')
if_new = functions.menu()

# Complete new budget
if if_new == 'Register':
    username = login_function.new_user()

    your_name = username

    print(f'Hello there {your_name}, lets get down to saving you money!')

    your_income = functions.pay_timetable()

    functions.save_income(username, your_income)

    clearing.clear()

    p1 = budget.Budget(your_name, your_income)

    functions.adding_expenses(p1)

    clearing.clear()

    spare = p1.spare_cash()

    functions.saving_expenses(username, p1)

# Use previously saved data to calculate data
elif if_new == 'Existing User':
    username = login_function.current_user()
    your_name = username
    
    
    print(f'Hello there {your_name}, lets get down to saving you money!')
    # Finding the income of user
    saved_income = input('Would you like to use your saved income? (y/n): ')
    if saved_income == 'n':
        your_income = functions.pay_timetable()
        # Create new Saved income file
        functions.save_income(username, your_income)
        
    elif saved_income == 'y':
        your_income = functions.open_income(username)
        

    p1 = budget.Budget(your_name, your_income)
    # Finding the users expenses 
    saved_expenses = input('Would you like to use your saved expenses? (y/n): ')
    if saved_expenses == 'y':
        functions.open_expenses(username, p1)
        
    elif saved_expenses == 'n':
        functions.adding_expenses(p1)

    clearing.clear()

    spare = p1.spare_cash()
# let user quit
elif if_new == 'Quit':
    print('Goodbye!')
    quit()

# Display Table to show user breakdown of expenses against income and leftover money
functions.display_table(p1)

time.sleep(3)

# What feature would they like to do next?
print('There are more features to explore.')
# Loop to let user use each of the features as they want
while True:
    next_feature = functions.further_features()
    clearing.clear()
    if next_feature == 'Savings Calculator':
        clearing.clear()
        functions.savings_calculator()
    elif next_feature == 'Debt Relief Calculator':
        clearing.clear()
        functions.debt_calculator()
    # Delete current user and any saved data
    elif next_feature == 'Delete User Profile':
        clearing.clear()
        functions.delete_user(username)
        
    # let user quit
    elif next_feature == 'Quit':
        clearing.clear()
        print('Thank you for using this application, have a nice day!')
        quit()
