# Budgeting app
from budget import Budget

# Welcome and ask name
your_name = input("Welcome to your personal budgeting buddy. What is your name? ")

print(f'Well hello there {your_name}, lets get down to saving you money!')

your_income = float(input("What is your income after tax? "))

pay_timetable = input("Are you paid weekly, fortnightly, or monthly? (w/f/m) ")

if pay_timetable == 'm':
    your_income = your_income / 4
elif pay_timetable == 'f':
    your_income = your_income / 2

p1 = Budget(your_name, your_income)
