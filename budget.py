# from prettytable import PrettyTable

# Main Budgeting class to find simple budget

class Budget:

    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.expense_description = []
        self.expense_amount = []
        self.total_expenses = 0

    def set_expense(self, new_exp_des, new_exp_amount):
        self.expense_description.append(new_exp_des.capitalize())
        self.expense_amount.append(new_exp_amount)
        self.total_expenses = self.total_expenses + new_exp_amount
        
    def spare_cash(self):
        self.spare = self.income - self.total_expenses
        print(f'You have ${self.spare} left to spend!')