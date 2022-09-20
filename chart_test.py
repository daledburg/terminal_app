from datetime import date


balance_owed = float(input('What is the balance owed on the outstanding debt? $'))
current_contribution = float(input('What is the current contribution to this debt? $'))
frequency_of_contribution = (input('Do you pay this expense weekly, fortnightly, monthly? (w/f/m) ')).lower()
    if frequency_of_contribution == 'f':
        frequency_of_contribution = round((current_contribution / 2), 2)
    elif frequency_of_contribution == 'm':
        amount_next_expense = round((current_contribution / 4), 2)

paid_date = input('When do you want to pay this off by? format: mm/yyyy ')
paid_date_ints = paid_date.split('/')

month_int = int(paid_date_ints[0])
year_int = int(paid_date_ints[1])

current_date = date.today()

current_date = str(current_date)

current_date_split = current_date.split('-')

current_year_int = int(current_date_split[0])
current_month_int = int(current_date_split[1])

months_to_pay = ((year_int - current_year_int) * 12) + (month_int - current_month_int)

contribution_needed = round(((balance_owed / months_to_pay) / 4), 2)

print(f'You currently only contribute ${current_contribution} each week.')
print(f'To meet your goal you need to contribute ${contribution_needed} per week')

