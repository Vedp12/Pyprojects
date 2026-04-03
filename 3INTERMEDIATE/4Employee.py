"""
### **Employee Management System**

**Objective:** Design a system to manage employees with different roles and payment structures.

### Requirements:

- Create an abstract base class `Employee` with:
    - Private attributes: `emp_name` (str), `employee_id` (str).
    - Abstract methods: `calculate_salary()`, `display_details()`.
- Create derived classes: `FullTimeEmployee`, `PartTimeEmployee`, and `Contractor`.
    - `FullTimeEmployee` should have: `monthly_salary` (float).
    - `PartTimeEmployee` should have: `hours_worked` (int), `hourly_rate` (float).
    - `Contractor` should have: `project_fee` (float).
    - Override `calculate_salary()` for each class.
- Use **encapsulation** for all attributes and provide **getters and setters**.
- Demonstrate **polymorphism** by calculating salaries for a list of employees of different types.
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_name: str, employee_id: str, salary: float):
        self.__emp_name = emp_name
        self.__employee_id = employee_id
        self.salary = salary

    def salary1(self):
        return self.salary

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_detail(self):
        pass

    @property
    def emp_name_(self):
        return self.__emp_name

    @emp_name_.setter
    def emp_name_(self):
        if self.__emp_name == int:
            raise ValueError("The EMP Name is a string value not a INT")

    @property
    def emp_id_(self):
        return self.__employee_id

    @emp_id_.setter
    def emp_id_(self):
        if self.__employee_id == int:
            raise ValueError("This EMP ID is a string not a INT")


class FullTimeEmployee(Employee):
    def __init__(self, emp_name: str, employee_id: str, salary: float):
        super().__init__(emp_name, employee_id, salary)

    def calculate_salary(self):
        return self.salary

    def display_detail(self):
        print(f"\n{self.emp_name_} has {self.emp_id_} id with salary of {self.salary}")


class PartTimeEmployee(Employee):
    def __init__(self, emp_name: str, employee_id: str, salary: float):
        return super().__init__(emp_name, employee_id, salary)

    def calculate_salary(self, hours_worked: int):
        self.hours_worked = hours_worked
        self.salary *= hours_worked

    def display_detail(self):
        print(f"\n{self.emp_name_} has {self.emp_id_} id with salary of {self.salary}")


class Contractor(Employee):
    def __init__(self, emp_name: str, employee_id: str, salary: float):
        super().__init__(emp_name, employee_id, salary)

    def calculate_salary(self, no_of_project: int):
        self.no_of_project = no_of_project
        self.salary *= no_of_project

    def display_detail(self):
        print(f"\n{self.emp_name_} has {self.emp_id_} id with salary of {self.salary}")


P1 = FullTimeEmployee("Ved", "F20321", 50000.52)

P1.calculate_salary()
P1.display_detail()

P2 = PartTimeEmployee("Tux", "P856987", 5000)
P2.calculate_salary(2)
P2.display_detail()

P3 = Contractor("kay", "C8987456", 7000)
P3.calculate_salary(2)
P3.display_detail()
