class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        return f"{self.name} age is {self.__age} "


obj = Person("ved", 20)
print(obj.show())
