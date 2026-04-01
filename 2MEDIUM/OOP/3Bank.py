"""
**Objective:** Simulate a bank account system with multiple account types.

### Requirements:

- Create an abstract base class `Account` with:
    - Private attributes: `account_number` (string), `balance` (float).
    - Abstract methods: `deposit(amount)`, `withdraw(amount)`, `displaybalance()`.
    - Use **getters and setters** for `balance`.
- Create derived classes: `SavingsAccount` and `CurrentAccount`.
    - `SavingsAccount` should have an additional attribute: `interest_rate` (float).
        - Override `deposit()` to add interest.
    - `CurrentAccount` should have an additional attribute: `overdraft_limit` (float).
        - Override `withdraw()` to allow overdraft up to the limit.
- Demonstrate **polymorphism** by processing a list of accounts.

"""

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_name: str, balance: float):
        self.__account_name = account_name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, Value):
        if Value >= 0:
            self.__balance = Value
        else:
            raise ValueError("Digit can't be lower")

    def get_account_name_(self):
        return self.__account_name

    @abstractmethod
    def deposit(self, amount):

        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def display_info(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_name: str, balance: float, interest_rate=2.5):
        super().__init__(account_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        interest = (amount * self.interest_rate) / 100
        self.balance += amount + interest
        print(f"{self.balance} is deposit with interest of {self.interest_rate}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount withdraw {self.balance}")
        else:
            raise ValueError("Amount inefficient in bank")

    def display_info(self):
        return f"\n{self.get_account_name_()} has balance of {self.balance} in Savings account \n\n"


person1 = SavingsAccount("ved", 5000, 2.5)
person1.deposit(200)
person1.withdraw(300)
print(person1.display_info())
