
# Main Budgeting class to find simple budget

class Budget:

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def add_expense(self):
        expense_description = []
        expense_amount = []
        while True:
            x = input('Enter an expense? (y/n): ')
            if x == 'y':
                g = input('What is it? ')
                h = float(input('How much is it? '))
                expense_description.append(g)
                expense_amount.append(h)
            else:
                print(expense_description)
                print(expense_amount)
                return False

first = Budget('Dale', 1000)

first.add_expense()

# print(first.expense_description)
# print(first.expense_amount)