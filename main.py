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

while True:
    more_exp = input('Do you want to add an expense? (y/n): ')
    if more_exp == 'y':
        p1.set_expense((input('What is this expense? ')), (float(input('How much is this expense? '))))
    elif more_exp == 'n':
        break

print(sum(p1.expense_amount))

print(p1.income - sum(p1.expense_amount))
