# from prettytable import PrettyTable

# Main Budgeting class to find simple budget

class Budget:
    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.spare = 0
        self.expense_description = []
        self.expense_amount = []
        self.total_expenses = 0

    def set_expense(self, new_exp_des, new_exp_amount):
        self.expense_description.append(new_exp_des.capitalize())
        self.expense_amount.append(new_exp_amount)
        self.total_expenses = self.total_expenses + new_exp_amount

    def spare_cash(self):
        print(self.income)
        self.spare = self.income - sum(self.expense_amount)
        print(f'You have ${self.spare} left to spend every week!')

# Child class for savings goal calculations

class SavingGoal(Budget):
    def __init__(self, name, income, savings_goal, savings_time):
        super().__init__(name, income=income)
        self.savings_goal = savings_goal
        self.savings_time = savings_time
        # contribution_needed = 0

    def find_required_amount(self):
        contribution_needed = round(((self.savings_goal / self.savings_time) / 4), 2)
        print(f'You need to contribute ${contribution_needed} extra per week to reach your goal.')
