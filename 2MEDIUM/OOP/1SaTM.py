#Student and Teacher Managerment
from abc import ABC, abstractmethod 

class Person:
    def __init__(self,name: str,age: int):
        self.name   = name
        self.age    = age

class Student(Person):
    def __init__(self, student_id:str ,name: str, age: int):
        super().__init__(name, age)
        self.student_id = student_id
    
    def Display_info(self):
        return f"{self.name}'s age is {self.age} and Student ID is {self.student_id}"

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject
    def Display_info(self):
        return f"{self.name}'s age is {self.age} and subject is {self.subject}"

s1 = Student("iu2546879","ved",20)
print(s1.Display_info())
t1 = Teacher("V", 40, "Py")
print(t1.Display_info())
