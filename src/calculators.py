# Functions module for calculators
from datetime import date

# Current Date info
current_date = date.today()
current_date = str(current_date)
current_date_split = current_date.split('-')
current_date_split = [int(i) for i in current_date_split]
current_date_split = current_date_split[0:2]

# Savings Calculator feature function
def savings_calculator(goal_amount, month_int, year_int):
    months_to_pay = (((year_int - current_date_split[0]) * 12) + (month_int - current_date_split[1]))
    contribution_needed = round(((goal_amount / months_to_pay) / 4), 2)
    print(f'You will need to hide away ${contribution_needed} each week to reach your goal!')
    return contribution_needed

# Feature of debt calculator function
def debt_calculator(debt_amount, month_int, year_int, contribution):
    months_to_pay = ((year_int - current_date_split[0]) * 12) + (month_int - current_date_split[1])
    contribution_needed = round((debt_amount / (months_to_pay * 4)), 2)
    contribution_diff = round((contribution_needed - contribution), 2)
    print(f'You currently contribute ${contribution} each week.')
    print(f'To meet your goal you need to contribute ${contribution_needed} per week')
    print(f'That is a difference of ${contribution_diff}')
    return contribution_diff

# Function to get future date for calculators
def future_date(inp_str):
    while True:
        try:
            paid_date = input(f'When do you want to {inp_str} by? format: mm/yyyy ')
            paid_date_ints = paid_date.split('/')

            if len(paid_date_ints) == 2:
                paid_date_ints = [int(i) for i in paid_date_ints]
                if paid_date_ints[0] > 0 and paid_date_ints[0] <= 12:
                    if paid_date_ints[1] > 2021 and paid_date_ints[1] <= 2099:    
                        if paid_date_ints[1] > current_date_split[0]:
                            return paid_date_ints
                        elif paid_date_ints[1] == current_date_split[0]:
                            if paid_date_ints[0] > current_date_split[1]:
                                return paid_date_ints
        except ValueError:
            pass
        print('Enter future date in correct format: mm/yyyy ')
