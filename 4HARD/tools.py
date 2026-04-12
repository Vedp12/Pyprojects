class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, note=""):
        self.balance += amount
        self.transactions.append((amount, note))

    def withdraw(self, amount, note=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.transactions.append((-amount, note))
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def get_transactions(self):
        return self.transactions


class Expense(Budget):
    def __init__(self, name, budget, balance=0):
        super().__init__(name, balance)
        self.budget = budget

    def get_budget(self):
        return self.budget

    def get_balance_left(self):
        return self.budget - self.balance


def main():
    # create an expense budget
    expense_budget = Expense("Expense", 1000)

    # deposit money into the expense budget
    expense_budget.deposit(200, "Salary")

    # withdraw money from the expense budget
    expense_budget.withdraw(100, "Grocery shopping")

    # get the balance of the expense budget
    print(expense_budget.get_balance())

    # get the budget of the expense budget
    print(expense_budget.get_budget())

    # get the balance left in the expense budget
    print(expense_budget.get_balance_left())

    # get the transactions of the expense budget
    print(expense_budget.get_transactions())

if __name__ == '__main__':
    main()