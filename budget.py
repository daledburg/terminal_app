from prettytable import PrettyTable

# Main Budgeting class to find simple budget

class Budget:

    def __init__(self, name, income):
        self.name = name
        self.income = income

    def add_expense(self, income):
        expense_description = input('What is this expense? ')
        

    # def add_expense(self):
    #     expense_description = []
    #     expense_amount = []
    #     while True:
    #         x = input('Enter an expense? (y/n): ')
    #         if x == 'y':
    #             g = input('What is it? ')
    #             h = float(input('How much is it? '))
    #             expense_description.append(g)
    #             expense_amount.append(h)
    #         else:
    #             print(expense_description)
    #             print(expense_amount)
    #             # print(sum(expense_amount))
    #             spare = self.income - sum(expense_amount)
    #             print(f'You have ${spare} remaining for fun!')
    #             return False
        
t = input('What is your name? ')
p = float(input('What is your weekly income? '))

first = Budget(t.upper, p)

first.add_expense()

my_table = PrettyTable()

my_table.add_row([first.expense_description[0], expense_amount[0]])
my_table.add_row([expense_description[1], expense_amount[2]])
