"""
### **Employee Management System**

**Objective:** Design a system to manage employees with different roles and payment structures.

### Requirements:

- Create an abstract base class `Employee` with:
    - Private attributes: `name` (string), `employee_id` (string).
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


