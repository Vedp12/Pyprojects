class name:
    def __init__(self, age=0):
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, x=12):
        self.__age = x


raj = name()

# setting the age using setter
raj.set_age()

# retrieving age using getter
print(raj.get_age())

print(raj.__age)
